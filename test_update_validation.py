from passenger_manager import PassengerManager

manager = PassengerManager()
manager.register_passenger("Chinelo Kanu", "57712345")

print("Trying to update to an empty name:")
result = manager.update_passenger(1, name="")
print(result)

print("\nTrying to update to an invalid phone number:")
result = manager.update_passenger(1, phone="abc123")
print(result)

print("\nUpdating to valid new values:")
result = manager.update_passenger(1, phone="59900112")
print(result)

manager.display_passengers()
