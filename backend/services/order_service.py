from models import db, Myorder

def place_order(customer_id, delivery_location):
    order = Myorder(customer_id=customer_id, delivery_location=delivery_location)
    db.session.add(order)
    db.session.commit()
    return order

def get_order_status(order_id):
    order = Myorder.query.get(order_id)
    if order:
        return order.status
    return "Order not found"
