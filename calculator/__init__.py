import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL", "sqlite:///" + os.path.join(app.root_path, "calculator.db"))
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
app.config["SESSION_PERMANENT"] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'
login_manager.login_message_category = "info"

from calculator import routes

@app.cli.command("init-db")
def init_db():
    """Create a fresh database without shipping user records in source control."""
    db.create_all()
