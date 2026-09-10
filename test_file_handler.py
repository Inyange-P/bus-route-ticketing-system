from passenger_manager import PassengerManager
from utils.file_handler import save_passengers, load_passengers

manager = PassengerManager()
manager.register_passenger("Chinelo Kanu", "57712345")
manager.register_passenger("Moses Kolaan", "58899221")

print("saving passengers to file...")
save_passengers(manager.passengers)

print("\nloading passengers back:")
loaded_passengers = load_passengers()
for passenger in loaded_passengers.values():
    print(passenger)