

def validate_body_data(data):
    base_keys = ["email", "username", "ip_address", "created_at", "location", "device_info"]
    location_keys = ["latitude", "longitude", "city", "country"]
    device_info_keys = ["browser", "os", "device_id"]
    for key in base_keys:
        if key not in data:
            return False
    for key in location_keys:
        if key not in data["location"]:
            return False
    for key in device_info_keys:
        if key not in data["device_info"]:
            return False
    return True
