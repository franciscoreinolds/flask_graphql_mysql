# app/models/Skill.py

from app import db

class Skill(db.Model):
    __tablename__ = "skills"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    score = db.Column(db.Integer)
    profile_id = db.Column(db.Integer, db.ForeignKey("profiles.id"))

    def __repr__(self):
        return f"<Skill {self.name} with score {self.score}>"
