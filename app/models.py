import hashlib
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    password = db.Column(db.String(255), index=True)
    email = db.Column(db.String(120), index = True, unique = True)

    def __init__(self, login, password):
        self.nickname = login
        self.password = User.get_hash_password(password)

    def __repr__(self):
        return '<User {nick}>'.format(nick=self.nickname)

    @staticmethod
    def get_hash_password(password):
        return hashlib.sha512(password.encode('utf-8')).hexdigest()