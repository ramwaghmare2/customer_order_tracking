from flask import Blueprint, request, jsonify, render_template, flash, url_for, redirect
from models.customer import Customer
from models.order import Myorder
from services.order_service import place_order, get_order_status
from kafka_producer import produce_message
from models import db
import requests

bp = Blueprint('customer_routes', __name__)

# Route to handle order form submission
HERE_API_KEY = 'y24ahK7VnVrMkaDdBKCQVKKsNi2P8zTp3E-IHzmyfrQ'  # Replace with your actual HERE API key

@bp.route("/place_order", methods=["POST"])
def place_order_route():
    try:
        # Get data from the form
        customer_id = request.form['customerId']
        delivery_location = request.form['location']

        # Fetch customer details from the database
        customer = Customer.query.get(customer_id)

        if not customer:
            flash("Customer not found", "error")
            return redirect(url_for('customer_routes.add_customer_form'))  # Redirect to customer form

        # Use customer's address if delivery location is not provided
        if not delivery_location:
            delivery_location = customer.address

        # Set current location to the customer's address
        current_location = customer.address

        # Geocode delivery location using HERE Maps API
        geocode_url = f"https://geocode.search.hereapi.com/v1/geocode?q={delivery_location}&apiKey={HERE_API_KEY}"

        geocode_response = requests.get(geocode_url)
        geocode_data = geocode_response.json()

        if geocode_data and 'items' in geocode_data and len(geocode_data['items']) > 0:
            # Extract latitude and longitude
            latitude = geocode_data['items'][0]['position']['lat']
            longitude = geocode_data['items'][0]['position']['lng']
        else:
            flash("Failed to get coordinates for the delivery location", "error")
            return redirect(url_for('customer_routes.add_customer_form'))

        # Create a new order with geocoded location
        new_order = Myorder(
            customer_id=customer_id,
            delivery_location=delivery_location,
            current_location=current_location,  # Assuming this column exists in Myorder
        )

        # Add new order to the database
        db.session.add(new_order)
        db.session.commit()

        # Produce Kafka message for order processing, including latitude and longitude
        order_details = {
            'customer_id': customer_id,
            'name': customer.name,
            'email': customer.email,
            'order_id': new_order.id,
            'delivery_location': delivery_location,
            'coordinates': {
                'latitude': latitude,
                'longitude': longitude
            },
            'status': 'Order Placed'
        }
        produce_message('order_topic', order_details)

        # Flash success message and redirect to the map for location tracking
        success_message = "Order placed successfully!"
        return redirect(url_for('map_view', delivery_location=delivery_location, latitude=latitude, longitude=longitude))

    except Exception as e:
        flash(f"An error occurred: {str(e)}", "error")
        return redirect(url_for('customer_routes.add_customer_form'))


# Route to get order status
@bp.route("/order_status/<int:order_id>", methods=["GET"])
def order_status_route(order_id):
    status = get_order_status(order_id)
    return jsonify({'order_status': status})


# Route to add a new customer
@bp.route("/add_customer", methods=["POST"])
def add_customer():
    try:
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']

        # Create and add a new customer
        new_customer = Customer(name=name, email=email, address=address)
        db.session.add(new_customer)
        db.session.commit()

        flash('Customer added successfully!', 'success')
        return redirect(url_for('customer_routes.add_customer_form'))
    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'error')
        return redirect(url_for('customer_routes.add_customer_form'))


# Route to display the customer form
@bp.route("/add_customer_form", methods=["GET"])
def add_customer_form():
    return render_template('add_customer.html')
