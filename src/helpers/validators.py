def validate_form_data(data):
    """Validate extracted form data."""
    required_fields = ["patient_name", "dob", "date"]
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")
    return data