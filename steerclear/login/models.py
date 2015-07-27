from steerclear import db
from flask.ext import login

class User(db.Model, login.UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(120))

    def __repr__(self):
        return "User(ID %r, Username %r, Password %r)" % (
            self.id,
            self.username,
            self.password
        )
