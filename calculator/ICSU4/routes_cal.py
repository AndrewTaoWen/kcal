import flask_bcrypt
from calculator import app
from flask import render_template, redirect, url_for, flash, request
from calculator.models import Item, User
from calculator.forms_cal import BudgetForm, IntakeForm, ExpenditureForm, RegisterForm, LoginForm
from calculator.dtos_cal import BudgetDTO
from calculator.services_cal import Calculator
from calculator import db
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/test")
def test_page():
    return render_template("test.html")


@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home_cal.html")

@app.route("/budget", methods=['GET', 'POST'])
def budget_page():
    form = BudgetForm()
    print(form.errors)
    if form.validate_on_submit():
        print(f'call calculateBudget() function: {form.age.data}, {form.gender.data}, {form.height.data}, {form.weight.data}, {form.activity.data}')
        budget = BudgetDTO(
            age=form.age.data,
            gender=form.gender.data,
            height=form.height.data,
            weight=form.weight.data,
            activity=form.activity.data
        )
        print(budget, Calculator.calculateBudget(budget))
        calculatedBudget = Calculator.calculateBudget(budget)
        form.budget.data = calculatedBudget
    else:
        for key, err_msg in form.errors.items():
            print(key, err_msg)
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template("budget_cal.html", form=form)

@app.route("/intake", methods=['GET', 'POST'])
def intake_page():
    form = IntakeForm()

    print(form.b1.data)

    return render_template("intake_cal.html", form=form)

@app.route("/expenditure", methods=['GET', 'POST'])
def expenditure_page():
    form = ExpenditureForm()

    print(form.b1.data)

    return render_template("expenditure_cal.html", form=form)

@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()

    print(form.username.data)

    return render_template("register_cal.html", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    # if form.validate_on_submit():
    #     attempted_user = User.query.filter_by(username=form.username.data).first()
    #     if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
    #         login_user(attempted_user)
    #         flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
    #         return redirect(url_for('market_page'))
    #     else:
    #         flash('Username and password are not matched! Please try again', category='danger')
    return render_template('login_cal.html', form=form)
