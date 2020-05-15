# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash

from .extensions import db


class Idea(db.Model):
    tablename = 'Idea'
    id = db.Column(db.Integer, primary_key=True)
    what = db.Column(db.Text)
    how = db.Column(db.Text)
