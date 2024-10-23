from flask import Flask, render_template, redirect, jsonify, request
from flask_socketio import SocketIO, emit
from routes import customer_routes
from kafka_producer import produce_message
from kafka_consumer import consume_messages,consume_delivery_location
from config import Config  # Import the config class
from models import init_db, db
from flask_migrate import Migrate
import os
import threading

app = Flask(__name__, template_folder='../frontend')

app.config.from_object(Config)
socketio = SocketIO(app)

delivery_boy_location = {"lat": 0, "lng": 0}

try:
    init_db(app)  # Initialize the db here
    migrate = Migrate(app, db)
except Exception as e:
    print(f"Database initialization error: {e}")

# Register customer routes
app.register_blueprint(customer_routes.bp)

@app.route("/")
def base():
    return render_template('index.html')

# Route to update delivery boy location (called by delivery boy system)
@app.route('/update_location', methods=['POST'])
def update_location():
    global delivery_boy_location
    # Get new location from the delivery boy's post request (e.g., {"lat": ..., "lng": ...})
    new_location = request.get_json()
    
    # Update delivery boy's location
    delivery_boy_location['lat'] = new_location.get('lat')
    delivery_boy_location['lng'] = new_location.get('lng')
    
    # Emit the new location to all connected clients (i.e., customers)
    socketio.emit('location_update', delivery_boy_location)
    
    return jsonify({"status": "success"}), 200

@app.route("/map")
def map_view():
    delivery_location = request.args.get('delivery_location')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    return render_template("map.html", delivery_location=delivery_location, latitude=latitude, longitude=longitude)


# Handle WebSocket connections
@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')


@app.route("/add_customer_form")
def add_customer_form():
    return render_template('add_customer.html')

def start_kafka_consumer():
    with app.app_context():
        consume_messages(socketio)

def start_delivery_location_consumer():
    with app.app_context():
        consume_delivery_location(socketio)

if __name__ == "__main__":
        # Thread for order update consumer
        consumer_thread = threading.Thread(target=start_kafka_consumer)
        consumer_thread.daemon = True 
        consumer_thread.start()

        # Thread for delivery location consumer
        location_thread = threading.Thread(target=start_delivery_location_consumer)
        location_thread.daemon = True
        location_thread.start()

        socketio.run(app, debug=True)
