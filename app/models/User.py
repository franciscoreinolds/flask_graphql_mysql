# app/models/User.py

from app import db

# Models

from app.models.Profile import Profile as Profile

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(256), index=True, unique=True)
    name = db.Column(db.String(256))
    last_name = db.Column(db.String(256))
    profile_id = db.Column(db.Integer, db.ForeignKey("profiles.id"))
    profile = db.relationship("Profile")

    def __repr__(self):
        return f"<User {self.username}>"