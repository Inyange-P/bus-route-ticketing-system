from bus_pass_manager import BusPassManager

manager = BusPassManager()

manager.issue_pass(1, "student", "2026-01-01", "2027-01-01")

print("Before status change:")
manager.display_passes()

manager.set_pass_status(1, "suspended")

print("\nAfter suspending the bus pass:")
manager.display_passes()

print("\nChecking if a suspended pass is still valid for travel:")
print(manager.is_pass_valid(1, "2026-06-15"))  # Expected: (False, "Bus pass is suspended.")

manager.set_pass_status(1, "cancelled")

print("\nAfter cancelling the bus pass:")
manager.display_passes()