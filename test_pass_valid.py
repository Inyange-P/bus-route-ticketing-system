from bus_pass_manager import BusPassManager

manager = BusPassManager()

manager.issue_pass(1, "student", "2026-01-01", "2027-01-01")

print("Checking a valid pass (travel before expiry):")
print(manager.is_pass_valid(1, "2026-06-15"))  # Expected: (True, "Bus pass is valid.")

print("\nChecking an expired pass (travel after expiry):")
print(manager.is_pass_valid(1, "2027-01-15"))  # Expected: (False, "Bus pass has expired.")

print("\nChecking a pass ID that does not exist:")
print(manager.is_pass_valid(99, "2026-06-15"))  # Expected: (False, "Bus pass not found.")