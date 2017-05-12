"""
user model
"""

from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password_hash = db.Column(db.String(100))

    @property
    def password(self):
        raise ValueError('Password is not accessible')

    @password.setter
    def password(self, password: str) -> None:
        """
        save password hash
        :param password: raw password
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        """
        check if password is right
        :param password: raw password
        :return: wether password is right
        """
        return check_password_hash(self.password_hash, password)
