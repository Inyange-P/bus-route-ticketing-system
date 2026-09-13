from passenger_manager import PassengerManager

manager = PassengerManager()

print("Registering a passenger with valid details:")
p1 = manager.register_passenger("Chinelo Kanu", "57712345")
print(p1)

print("\nRegistering a passenger with an empty name:")
p2 = manager.register_passenger("", "57712345")
print(p2)

print("\nRegistering a passenger with an invalid phone number:")
p3 = manager.register_passenger("Abigail Inyang", "abc12345")
print(p3)

manager.display_passengers()

