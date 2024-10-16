from kafka import KafkaProducer
import json

def get_kafka_producer():
    return KafkaProducer(
        bootstrap_servers='customer_order_kafka:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

def produce_message(topic, message):
    producer = get_kafka_producer()
    print(f"Producing message to topic '{topic}': {message}")
    producer.send(topic, message)
    producer.flush()
