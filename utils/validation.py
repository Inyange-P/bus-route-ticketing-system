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

