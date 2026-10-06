from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime, timedelta, timezone
import secrets

TOKEN_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    rod = db.Column(db.String(50))
    reset_token = db.Column(db.String(100), nullable=True)
    reset_token_expires = db.Column(db.String(19))

    @staticmethod
    def verify_reset_token(token):
        now = datetime.now(timezone.utc).strftime(TOKEN_TIME_FORMAT)
        return User.query.filter(User.reset_token == token, User.reset_token_expires > now).first()

    def generate_reset_token(self):
        self.reset_token = secrets.token_urlsafe(32)
        expires = datetime.now(timezone.utc) + timedelta(hours=1)
        self.reset_token_expires = expires.strftime(TOKEN_TIME_FORMAT)
        db.session.commit()
        return self.reset_token