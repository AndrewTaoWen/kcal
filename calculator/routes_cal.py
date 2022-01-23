import flask_bcrypt
from calculator import app
from flask import render_template, redirect, url_for, flash, request, session
from calculator.models_cal import User, TrackingHistory
from calculator.forms_cal import BudgetForm, IntakeForm, ExpenditureForm, RegisterForm, LoginForm, HistoryForm
from calculator.calculator_cal import calculate_budget
from calculator import db
from flask_login import login_user, logout_user, login_required, current_user

@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home_cal.html")

@app.route("/budget", methods=['GET', 'POST'])
def budget_page():

    form = BudgetForm()

    if current_user.is_authenticated:
        session['budget'] = current_user.budget

    if form.validate_on_submit():
        calculated_budget = calculate_budget(form)
        current_user.budget = calculated_budget
        db.session.commit()
        session.permanent = False
        session['budget'] = calculated_budget

    return render_template("budget_cal.html", form=form)

@app.route("/intake", methods=['GET', 'POST'])
def intake_page():

    form = IntakeForm()
    if form.validate_on_submit():
        # TODO Calculate expenditure
        intake = form.bread_amt.data * 100
        session['intake'] = intake
    return render_template("intake_cal.html", form=form)

@app.route("/expenditure", methods=['GET', 'POST'])
def expenditure_page():

    form = ExpenditureForm()

    if form.validate_on_submit():
        # TODO Calculate expenditure
        expenditure = form.volleyball_amt.data * 15
        session['expenditure'] = expenditure

    return render_template("expenditure_cal.html", form=form)

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

    return render_template("register_cal.html", form=form)

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
    return render_template('login_cal.html', form=form)

@app.route('/logout')
def logout_page():
    session.clear()
    logout_user()
    flash('You have been logged out', category='info')
    return redirect(url_for('home_page'))

@app.route("/history", methods=['GET', 'POST'])
@login_required
def history_page():

    form = HistoryForm()
    history = TrackingHistory.query.filter_by(userid=current_user.id).order_by(TrackingHistory.tracking_date.desc())

    if request.method == 'POST':
        print(form.tracking_date.data)
        h = history.filter_by(tracking_date=form.tracking_date.data).first()
        if not h:
            h = TrackingHistory(budget=current_user.budget,
                                intake=session['intake'],
                                expenditure=session['expenditure'],
                                userid=current_user.id,
                                tracking_date=form.tracking_date.data)
            db.session.add(h)
        else:
            h.budget = current_user.budget
            h.intake = session['intake']
            h.expenditure = session['expenditure']
        db.session.commit()

    return render_template("history_cal.html", history=history, form=form)
