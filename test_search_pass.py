from bus_pass_manager import BusPassManager

manager = BusPassManager()

manager.issue_pass(1, "student", "2026-01-01", "2027-01-01")
manager.issue_pass(2, "priority", "2026-01-01", "2027-01-01")

print("Searching for bus pass with ID 1:")
results = manager.search_pass(pass_id=1)
for bus_pass in results:
    print(bus_pass)

print("\nSearching for bus pass for passenger with ID 2:")
results = manager.search_pass(passenger_id=2)
for bus_pass in results:
    print(bus_pass)

print("\nSearching for a nonexistent bus pass:")
results = manager.search_pass(pass_id=99)
if not results:
    print("No matching bus pass found.")
