from kafka import KafkaConsumer
import json
from flask_socketio import SocketIO,emit

def get_kafka_consumer():
    return KafkaConsumer(
        'order_status',
        bootstrap_servers='customer_order_kafka:9092',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

def consume_messages(socketio):
    consumer = get_kafka_consumer()
    for message in consumer:
        print(f"Received message: {message.value}")
        socketio.emit('order_update',message.value)