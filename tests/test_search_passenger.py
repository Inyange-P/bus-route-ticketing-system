from passenger_manager import PassengerManager

manager = PassengerManager()

manager.register_passenger("Chinelo Kanu", "57712345")
manager.register_passenger("Moses Kolaan", "58899221")

print("Searching for Chinelo Kanu:")

results = manager.search_passenger(name="Chinelo Kanu")

for passenger in results:
    print(passenger)

print("\nSearching using lowercase:")

results = manager.search_passenger(name="chinelo kanu")

for passenger in results:
    print(passenger)

print("\nSearching for a passenger that does not exist:")

results = manager.search_passenger(name="Nobody")

if not results:
    print("No matching passenger found.")