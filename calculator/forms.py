from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, SelectField, IntegerField, BooleanField, PasswordField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, NumberRange, Length, Email, EqualTo, ValidationError
from calculator.routes import User
from datetime import datetime

class BudgetForm(FlaskForm):

    activities = [(1, 'Sedentary: little or no exercise'),
                       (2, 'Light: exercise 1-3 times/week'),
                       (3, 'Moderate: exercise 4-5 times/week'),
                       (4, 'Active: daily exercise or intense exercise 3-4 times/week'),
                       (5, 'Very Active: intense exercise 6-7 times/week')]

    # (6, 'Extra Active: very intense exercise daily, or physical job')

    age = IntegerField(label='Age', default=25, validators=[NumberRange(min=15, max=80, message="Ages 15-80")])
    gender = RadioField('Gender', choices=[('m', 'Male'), ('f', 'Female')], default='m')
    height = IntegerField('Height', default="175", validators=[NumberRange(min=1, message="Height > 0")])
    weight = IntegerField('Weight', default="65", validators=[NumberRange(min=1, message="Weight > 0")])
    activity = SelectField('Activity', choices=activities, default=3)
    budget = StringField('Budget')
    submit = SubmitField('Calculate')

class IntakeForm(FlaskForm):

    bread_amt = IntegerField(label="Bread", default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    bagel_amt = IntegerField(label="Bagel", default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    egg_amt = IntegerField(label="Egg", default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    bacon_amt = IntegerField(label="Bacon", default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    yogurt_amt = IntegerField(label="Yogurt", default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    cereal_amt = IntegerField(label="Cereal", default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    oats_amt = IntegerField(label="Oats", default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    othersB_amt = IntegerField(label="Others", default=0, validators=[NumberRange(min=0, message="Amount >= 0")])

    pizza_amt = IntegerField(label="Pizza", default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    pasta_amt = IntegerField(label="Pasta", default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    sandwich_amt = IntegerField(label="Sandwich", default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    burger_amt = IntegerField(label="Burger", default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    beef_amt = IntegerField(label="Beef", default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    chicken_amt = IntegerField(label="Chicken", default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    pork_amt = IntegerField(label='Pork', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    othersL_amt = IntegerField(label='Others', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])

    pizzaD_amt = IntegerField(label='Pizza', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    pastaD_amt = IntegerField(label='Pasta', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    rice_amt = IntegerField(label='Rice', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    porkD_amt = IntegerField(label='Pork', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    beefD_amt = IntegerField(label='Beef', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    chickenD_amt = IntegerField(label='Chicken', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    potato_amt = IntegerField(label='Potato', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    othersD_amt = IntegerField(label='Others', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])

    submit = SubmitField(label='Calculate')

class ExpenditureForm(FlaskForm):

    walking_amt = IntegerField(label='Walking', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    jogging_amt = IntegerField(label='Jogging', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    running_amt = IntegerField(label='Running', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    biking_amt = IntegerField(label='Biking', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    swimming_amt = IntegerField(label='Swimming', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    basketball_amt = IntegerField(label='Basketball', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    soccer_amt = IntegerField(label='Soccer', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    badminton_amt = IntegerField(label='Badminton', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    football_amt = IntegerField(label='Football', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    tennis_amt = IntegerField(label='Tennis', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    baseball_amt = IntegerField(label='Baseball', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    tabletennis_amt = IntegerField(label='Table Tennis', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    volleyball_amt = IntegerField(label='Volleyball', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    hockey_amt = IntegerField(label='Hockey', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    lifting_amt = IntegerField(label='Weight Lifting', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    martialarts_amt = IntegerField(label='Martial Arts', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    golf_amt = IntegerField(label='Golf', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    others_amt = IntegerField(label='Others', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    skippingrope_amt = IntegerField(label='Skipping Rope', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    dancing_amt = IntegerField(label='Dancing', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    calisthenics_amt = IntegerField(label='Calisthenics', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    HIIT_amt = IntegerField(label='HIIT', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    skiing_amt = IntegerField(label='Skiing', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    snowboarding_amt = IntegerField(label='Snowboarding', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])
    submit = SubmitField(label='Calculate', default=0, validators=[NumberRange(min=0, message="Amount >= 0")])

class RegisterForm(FlaskForm):
    def validate_username(self, user_to_check):
        user = User.query.filter_by(username=user_to_check.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please use a different email address')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1', message="Passwords do not match"), DataRequired()])
    submit = SubmitField(label='Create Account')

class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    error_msg = StringField(label='Error', default = '')
    submit = SubmitField(label='Sign in')

class HistoryForm(FlaskForm):
    tracking_date = DateField(label='Enter Tracking Date:', default=datetime.today, validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField(label='Save to tracking history')

