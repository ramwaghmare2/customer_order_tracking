import os
import secrets  # to generate a strong secret key

class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/customer_order_tracking'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    KAFKA_SERVER = os.getenv('KAFKA_SERVER', 'customer_order_kafka:9092')

    # Add a SECRET_KEY for session management
    SECRET_KEY = os.getenv('SECRET_KEY', secrets.token_hex(16))  # generates a secure random key
