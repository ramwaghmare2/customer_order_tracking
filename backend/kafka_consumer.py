from kafka import KafkaConsumer
import json
from flask_socketio import SocketIO,emit

# Kafka Consumer for order status updates
def get_kafka_consumer():
    return KafkaConsumer(
        'order_status',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

# Kafka Consumer for delivery location updates
def get_kafka_consumer_delivery_location():
    return KafkaConsumer(
        'delivery_location_updates',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
# Function to listen for order status messages and emit via Socket.IO
def consume_messages(socketio):
    consumer = get_kafka_consumer()
    for message in consumer:
        print(f"Received message: {message.value}")
        socketio.emit('order_update',message.value)

# Function to listen for delivery location messages and emit via Socket.IO
def consume_delivery_location(socketio):
    consumer = get_kafka_consumer_delivery_location()
    for message in consumer:
        print(f"Received delivery location message: {message.value}")
        socketio.emit('location_update', message.value)