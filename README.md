# Customer Order Tracking & Delivery Boy Tracking System

## Overview

This system consists of two main components: 
1. **Customer Order Tracking**: Allows customers to place orders, track order statuses, and view real-time locations of the delivery person.
2. **Delivery Boy Tracking**: Enables delivery boys to accept or reject orders, view customer details, and provide real-time updates on their location during delivery.

Both components communicate with each other using Kafka to exchange real-time order and delivery status updates. The system is built with Flask, Kafka, MySQL, and Docker, and is deployed on AWS EC2.

## Project Structure

### 1. Customer Order Tracking
![image](https://github.com/user-attachments/assets/a2dc1b01-6b35-43d1-ad67-c8eece314ac4)


```

### 2. Delivery Boy Tracking

```
![image](https://github.com/user-attachments/assets/24cd44f2-cf19-486f-96dc-75e3dcafdb02)

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
