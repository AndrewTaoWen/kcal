from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, SelectField, IntegerField, BooleanField, PasswordField
from wtforms.validators import DataRequired, NumberRange, Length, Email, EqualTo
#, ValidationError, Length, EqualTo, Email,

class BudgetForm(FlaskForm):

    activities = [(1, 'Sedentary: little or no exercise'),
                       (2, 'Light: exercise 1-3 times/week'),
                       (3, 'Moderate: exercise 4-5 times/week'),
                       (4, 'Active: daily exercise or intense exercise 3-4 times/week'),
                       (5, 'Very Active: intense exercise 6-7 times/week'),
                       ]

    # (6, 'Extra Active: very intense exercise daily, or physical job')

    age = IntegerField(label='Age', default=25, validators=[NumberRange(min=15, max=80, message="Ages 15-80")])
    gender = RadioField('Gender', choices=[('m', 'Male'), ('f', 'Female')], default='m')
    height = IntegerField('Height', default="175")
    weight = IntegerField('Weight', default="65")
    activity = SelectField('Activity', choices=activities, default=3)
    budget = StringField('Budget')
    submit = SubmitField('Calculate')

class IntakeForm(FlaskForm):

    b1 = BooleanField(label="Bread")
    b1_amt = IntegerField()

    b2 = BooleanField(label="Milk")
    b2_amt = IntegerField()

    b3 = BooleanField(label="Egg")
    b3_amt = IntegerField()

    b4 = BooleanField(label="Bacon")
    b4_amt = IntegerField()

    b5 = BooleanField(label="Yogurt")
    b5_amt = IntegerField()

    submit = SubmitField('Calculate')

class ExpenditureForm(FlaskForm):

    b1 = BooleanField(label="Walking")
    b1_amt = IntegerField()

    b2 = BooleanField(label="Jogging")
    b2_amt = IntegerField()

    b3 = BooleanField(label="Running")
    b3_amt = IntegerField()

    b4 = BooleanField(label="Biking")
    b4_amt = IntegerField()

    b5 = BooleanField(label="Swimming")
    b5_amt = IntegerField()

    submit = SubmitField('Calculate')


class RegisterForm(FlaskForm):
    # def validate_username(self, user_to_check):
    #     user = User.query.filter_by(username = user_to_check.data).first()
    #     if user:
    #         raise ValidationError('Username already exists! Please try a different username')
    #
    # def validate_email_address(self, email_address_to_check):
    #     email_address = User.query.filter_by(email_address = email_address_to_check.data).first()
    #     if email_address:
    #         raise ValidationError('Email Address already exists! Please use a different email address')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')

