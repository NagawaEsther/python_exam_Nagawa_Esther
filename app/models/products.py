
from app import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    price_unit = db.Column(db.String(10), nullable=False, default='UGX')
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())


    def __init__(self, title, description, price,price_unit):
        self.title = title
        self.description = description
        self.price = price
        self.price_unit = price_unit
        
    def __repr__(self):
        return f'<Product {self.title}>'
