from utils.validation import validate_name, validate_phone, validate_passenger_exists

print("Testing a valid name:")
print(validate_name("Abigail Inyang"))

print("\nTesting an empty name:")
print(validate_name(""))

print("\nTesting a valid phone number:")
print(validate_phone("57712345"))

print("\nTesting an invalid phone number:")
print(validate_phone("abc123"))

print("\nTesting an existing passenger:")
print(validate_passenger_exists(1, {1: "Abigail"}))

print("\nTesting a passenger that does not exist:")
print(validate_passenger_exists(99, {1: "Flourish"}))