# Shared validation functions for the bus route and ticket management system
# Chinelo's section: Passenger and BusPass validation functions

def validate_name(name):
    # Validate that the name is a non-empty string.
    if not name or not name.strip():
        print("Invalid name: name cannot be empty.")
        return False
    return True

def validate_phone(phone):
    # Validate that the phone number is a string of digits and has a reasonable length.
    if not phone.isdigit():
        print("Invalid phone number: must contain digits only.")
        return False
    return True

def validate_passenger_exists(passenger_id, passengers):
    # Validate that the passenger exists in the system.
    if passenger_id not in passengers:
        print(f"Invalid passenger: passenger with ID {passenger_id} does not exist.")
        return False
    return True

def validate_phone(phone):
    # Validate that the phone number is a string of digits and has a reasonable length.
    phone = phone.strip()  # Remove leading and trailing whitespace
    if not phone.isdigit():
        print("Invalid phone number: must contain digits only.")
        return False
    if len(phone) < 7 or len(phone) > 15:
        print("Invalid phone number: length must be between 7 and 15 digits.")
        return False
    return True

def validate_pass_type(pass_type):
    # validate that the pass type is one of the allowed types.
    valid_pass_types = ["student", "senior", "priority"]
    if pass_type not in valid_pass_types:
        print(f"Invalid pass type: must be one of {valid_pass_types}.")
        return False
    return True

def validate_date_order(issue_date, expiry_date):
    # Validate that the issue date is before the expiry date.
    from datetime import datetime
    issue = datetime.strptime(issue_date, "%Y-%m-%d")
    expiry = datetime.strptime(expiry_date, "%Y-%m-%d")

    if expiry <= issue:
        print("Invalid dates: expiry date must be after issue date.")
        return False
    return True

