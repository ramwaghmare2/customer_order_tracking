# Customer Order Tracking & Delivery Boy Tracking System

## Overview

This system consists of two main components: 
1. **Customer Order Tracking**: Allows customers to place orders, track order statuses, and view real-time locations of the delivery person.
2. **Delivery Boy Tracking**: Enables delivery boys to accept or reject orders, view customer details, and provide real-time updates on their location during delivery.

Both components communicate with each other using Kafka to exchange real-time order and delivery status updates. The system is built with Flask, Kafka, MySQL, and Docker, and is deployed on AWS EC2.

## Project Structure

### 1. Customer Order Tracking
![image](https://github.com/user-attachments/assets/a2dc1b01-6b35-43d1-ad67-c8eece314ac4)

customer_order_tracking/
├── backend/
│   ├── app.py                      # Main Flask application for customer
│   ├── kafka_producer.py            # Kafka producer for placing orders and sending updates
│   ├── models/
│   │   ├── __init__.py             # SQLAlchemy setup
│   │   ├── customer.py             # Customer model
│   │   └── order.py                # Order model
│   └── routes/
│       └── customer_routes.py       # Customer-related routes
│   ├── services/
│       ├── order_service.py         # Logic for placing and tracking orders
│   ├── config.py                    # Configuration (Kafka, MySQL, etc.)
│   ├── requirements.txt             # Project dependencies
├── frontend/
│   ├── index.html                   # Main form for placing orders
│   ├── add_customer.html            # Form for adding a customer
│   ├── order_status.html            # Displays order status
│   ├── map.html                     # Displays real-time map with order tracking
│   ├── app.js                       # JavaScript logic for API calls and order management
│   └── api/
│       └── api.js                   # API calls for customer actions
├── docker/
│   ├── Dockerfile                   # Docker setup for customer system
│   ├── docker-compose.yml           # Docker Compose for managing services
└── README.md                        # Documentation for customer order tracking system
```

### 2. Delivery Boy Tracking

```
delivery_boy_tracking/
├── backend/
│   ├── app.py                      # Main Flask application for delivery boy
│   ├── kafka_consumer.py            # Kafka consumer for receiving customer orders
│   ├── kafka_producer.py            # Kafka producer for delivery status updates
│   ├── models/
│   │   ├── delivery_boy.py          # Delivery Boy model
│   │   └── order.py                # Order model (shared with customer)
│   └── routes/
│       ├── delivery_routes.py       # Delivery actions (accept/reject orders, update location)
│   ├── services/
│       ├── delivery_service.py      # Logic for order acceptance, location updates
│       ├── location_service.py      # Real-time location tracking
│   ├── config.py                    # Configuration (Kafka, MySQL, etc.)
│   ├── requirements.txt             # Project dependencies
├── frontend/
│   ├── delivery_home.html           # Home page for viewing and accepting/rejecting orders
│   ├── delivery_tracking.html       # Real-time delivery tracking page
│   ├── styles.css                   # Styling for delivery boy page
│   ├── app.js                       # JavaScript for API interactions and tracking
│   └── api/
│       └── api.js                   # API calls for delivery boy actions
├── docker/
│   ├── Dockerfile                   # Docker setup for delivery boy system
│   ├── docker-compose.yml           # Docker Compose for managing services
└── README.md                        # Documentation for delivery boy tracking system
```

---

## Features

### Customer Order Tracking:
- Customers can place orders by filling out a form.
- Track the status of their order in real-time.
- View delivery boy's location using a map.
  
### Delivery Boy Tracking:
- Delivery boys can view available orders and accept/reject them.
- Upon accepting an order, they receive customer details (customer name, location, etc.).
- Provide real-time location updates to customers during the delivery process.

### Real-Time Communication:
- Kafka is used to communicate between the customer and delivery boy services. Orders are produced by the customer system and consumed by the delivery boy system.
  
---

## Kafka Integration

- **Topics**: 
  - `order_topic`: Handles order placement and order status updates.
  - `delivery_topic`: Handles delivery boy's real-time location updates.

Kafka consumers and producers are integrated within the system to ensure real-time updates for both customers and delivery boys.

---

## Docker Setup

Both systems are containerized using Docker. To spin up the environment:

1. **Build the images**:
   ```
   docker-compose build
   ```

2. **Start the services**:
   ```
   docker-compose up
   ```

This will start:
- Flask applications for both customer and delivery boy systems.
- Kafka and Zookeeper services for message communication.
- MySQL databases for storing customer and order information.

---

## AWS EC2 Deployment

The application is deployed on AWS EC2 using Docker Compose. Each EC2 instance hosts:
- Kafka and Zookeeper
- The Flask applications for both customer and delivery boy services
- MySQL databases

### Steps for Deployment:
1. Set up EC2 instances with Docker and Docker Compose.
2. Upload the Docker Compose files and project folders to the EC2 instance.
3. Run the application using `docker-compose up` on each instance.

---

## Requirements

- Python 3.x
- Flask
- Kafka
- MySQL
- Docker & Docker Compose
- Leaflet.js for real-time maps (customer front end)

---

## How to Run Locally

1. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

2. **Start Kafka & Zookeeper** (locally):
   ```
   bin\windows\zookeeper-server-start.bat config\zookeeper.properties
   bin\windows\kafka-server-start.bat config\server.properties
   ```

3. **Start Flask applications** for both customer and delivery boy systems:
   ```
   python backend/app.py
   ```
