from . import db,ma
from flask_login import UserMixin
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    username = db.Column(db.String(80), )
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(255))
    posts = db.relationship('Post',backref='author',lazy='dynamic')
    
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email')
    
user_schema = UserSchema()
users_schema = UserSchema(many=True)
    
'''def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username'''