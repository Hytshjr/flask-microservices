from app import db

class Product(db.Model):
    __bind_key__ = "products_ms"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(90), nullable=False)
    name_detail = db.Column(db.String(120), default='name')
