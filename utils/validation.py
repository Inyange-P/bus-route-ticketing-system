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

def validate_status(status):
    # Validate that the status is either "active", "suspended", "cancelled".
    valid_statuses = ["active", "suspended", "cancelled"]
    if status not in valid_statuses:
        print(f"Invalid status: must be one of {valid_statuses}.")
        return False
    return True

def validate_positive_int(value):
    # Returns True only for a real positive whole number. 
    # In Python, bool is technically a subclass of int, so isinstance(True, int) is True. Without checking for bool separately, True/False could slip through and be mistaken for 1/0 wherever an ID or count is expected.
    if isinstance(value, bool):
        return False

    if not isinstance(value, int):
        return False

    return value > 0


def validate_record_exists(record_id, records):
    # Returns True if "records" is a dict-like collection (something that supports .get()) and it actually contains an entry for record_id. 
    # This one function covers "trip must exist", "passenger must exist", "route must exist", and "pass must exist" -- anywhere in the project where we're checking "is this ID present in this lookup table."
    if records is None:
        return False

    if not hasattr(records, "get"):
        return False

    return records.get(record_id) is not None


def validate_seat_number(seat_number, total_seats):
# Returns True if seat_number is a real positive integer that actually fits within the bus's seat range (1 up to total_seats).
    if not validate_positive_int(seat_number):
        return False

    if not validate_positive_int(total_seats):
        return False

    return seat_number <= total_seats