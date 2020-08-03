# app/models/Profile.py

from app import db

# Models

from app.models.Skill import Skill as Skill

class Profile(db.Model):
    __tablename__ = "profiles"
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(256))
    description = db.Column(db.Text)
    skills = db.relationship("Skill")

    def __repr__(self):
        return f"<Profile {self.role}>"
