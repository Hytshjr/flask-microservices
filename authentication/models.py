from app import db

class Users(db.Model):
    __bind_key__ = "users_ms"

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(90), nullable=False)
    user_name_detail = db.Column(db.String(120), default='name')
