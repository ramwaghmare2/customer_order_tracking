from . import db

class Myorder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Order Placed')
    delivery_boy_id = db.Column(db.Integer, nullable=True)
    delivery_location = db.Column(db.String(200), nullable=True)
    current_location = db.Column(db.String(200), nullable=True)
