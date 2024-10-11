def validate_order_data(data):
    required_fields = ['customer_id', 'delivery_location']
    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: {field}"
    return True, "Valid data"
