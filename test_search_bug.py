from passenger_manager import PassengerManager

manager = PassengerManager()
manager.register_passenger("Chinelo Kanu", "57712345")
manager.register_passenger("John Doe", "57767890")

print("Searching for a passenger with a correct ID and matching name:")
results = manager.search_passenger(passenger_id=1, name="Chinelo Kanu")
for passenger in results:
    print(passenger)

print("\nSearching by ID 1 but a name that belongs to someone else:")
results = manager.search_passenger(passenger_id=1, name="Jason")
if not results:
    print("No matching passenger found.")
else:
    for passenger in results:
        print(passenger)