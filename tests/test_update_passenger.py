from passenger_manager import PassengerManager

manager = PassengerManager()

manager.register_passenger("Chinelo Kanu", "57712345")

print("Before update:")
manager.display_passengers()

manager.update_passenger(1, phone="59900112")

print("\nAfter update:")
manager.display_passengers()