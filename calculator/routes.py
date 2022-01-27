import flask_bcrypt
from calculator import app
from flask import render_template, redirect, url_for, flash, request, session
from calculator.models import User, TrackingHistory
from calculator.forms import BudgetForm, IntakeForm, ExpenditureForm, RegisterForm, LoginForm, HistoryForm
from calculator.calculator import calculate_budget, calculate_intake, calculate_expen
from calculator import db
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/budget", methods=['GET', 'POST'])
def budget_page():

    form = BudgetForm()

    if current_user.is_authenticated:
        session['budget'] = current_user.budget
    elif 'budget' not in session:
        session['budget'] = 0

    if form.validate_on_submit():
        session['weight'] = form.weight.data
        calculated_budget = calculate_budget(form)
        current_user.budget = calculated_budget
        db.session.commit()
        session.permanent = False
        session['budget'] = calculated_budget

    return render_template("budget.html", form=form)

@app.route("/intake", methods=['GET', 'POST'])
def intake_page():

    if 'intake' not in session:
        session['intake'] = 0

    form = IntakeForm()
    if form.validate_on_submit():
        intake = calculate_intake(form)
        session['intake'] = intake
    return render_template("intake.html", form=form)

@app.route("/expenditure", methods=['GET', 'POST'])
def expenditure_page():

    form = ExpenditureForm()
    if 'weight' not in session:
         session['weight'] = 65

    if 'expenditure' not in session:
        session['expenditure'] = 0

    if form.validate_on_submit():
        expenditure = calculate_expen(form, session['weight'])
        session['expenditure'] = expenditure

    return render_template("expenditure.html", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        return redirect(url_for('budget_page'))

    return render_template("register.html", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            return redirect(url_for('budget_page'))
        else:
            form.error_msg.data = 'Username and password are not matched! Please try again'
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    session.clear()
    logout_user()
    return redirect(url_for('home_page'))

@app.route("/history", methods=['GET', 'POST'])
@login_required
def history_page():

    form = HistoryForm()
    history = TrackingHistory.query.filter_by(userid=current_user.id).order_by(TrackingHistory.tracking_date.desc())

    if request.method == 'POST':
        h = history.filter_by(tracking_date=form.tracking_date.data).first()
        if not h:
            h = TrackingHistory(budget=current_user.budget,
                                intake=session['intake'] or 0,
                                expenditure=session['expenditure'] or 0,
                                userid=current_user.id,
                                tracking_date=form.tracking_date.data)
            db.session.add(h)
        else:
            h.budget = current_user.budget
            h.intake = session['intake'] or 0
            h.expenditure = session['expenditure'] or 0
        db.session.commit()

    return render_template("history.html", history=history, form=form)
