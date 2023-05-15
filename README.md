# KCAL Calorie Counter Application

A personal project of calorie counting and tracking. (https://kcal-cc.herokuapp.com/)

## Installation

First, you need to clone this repository:

```bash
$ git clone https://github.com/AndrewTaoWen/kcal.git
```

Then change into the `kcal` folder:

```bash
$ cd kcal
```

Now, we will need to create a virtual environment and install all the dependencies:

```bash
$ python3 -m venv venv  # on Windows, use "python -m venv venv" instead
$ . venv/bin/activate  # on Windows, use "venv\Scripts\activate" instead
$ deactivate # deactivate virtual environment
$ pip install -r requirements.txt # install all required libraries
```
## How to Run the Application?

**Before running the application, make sure you have activated the virtual environment.**

```bash
python3 wsgi.py # on Windows, user "python wsgi.py"
```

## Miscellaneous Info

Manually install required libraries

```bash
pip install flask
pip install flask-sqlalchemy
pip install flask-wtf
pip install wtforms
pip install email_validator
pip install bcrypt
pip install flask_bcrypt
pip install flask_login
```

Generate requirement file for all required libraries
```bash
pip freeze > requirements.txt
```

Resources referenced during the creation of this project

https://www.youtube.com/watch?v=Qr4QMBUPxWo&t=18714s
https://github.com/jimdevops19/FlaskSeries
https://github.com/flatcoke/flask-structure
https://www.twilio.com/docs/usage/tutorials/how-to-set-up-your-python-and-flask-development-environment
https://github.com/greyli/flask-examples
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
