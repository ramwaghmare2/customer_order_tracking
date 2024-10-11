from geopy.distance import geodesic

def calculate_distance(location1, location2):
    return geodesic(location1, location2).meters

def notify_customer_distance(customer_location, delivery_boy_location):
    distance = calculate_distance(customer_location, delivery_boy_location)
    if distance < 50:
        return "Delivery boy is near you!"
    return f"Delivery boy is {distance:.2f} meters away"
