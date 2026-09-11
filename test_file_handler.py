from passenger_manager import PassengerManager
from bus_pass_manager import BusPassManager
from utils.file_handler import save_passengers, load_passengers, save_bus_passes, load_bus_passes

manager = PassengerManager()
manager.register_passenger("Chinelo Kanu", "57712345")
manager.register_passenger("Moses Kolaan", "58899221")

print("Saving passengers to file...")
save_passengers(manager.passengers)

print("\nloading passengers back:")
loaded_passengers = load_passengers()
for passenger in loaded_passengers.values():
    print(passenger)

pass_manager = BusPassManager()
pass_manager.issue_pass(1, "student", "2026-01-01", "2027-01-01")

print("\nSaving bus passes to file...")
save_bus_passes(pass_manager.bus_passes)

print("\nLoading bus passes back:")
loaded_passes = load_bus_passes()
for bus_pass in loaded_passes.values():
    print(bus_pass)
    