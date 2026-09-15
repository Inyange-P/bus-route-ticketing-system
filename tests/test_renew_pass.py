from bus_pass_manager import BusPassManager

manager = BusPassManager()

manager.issue_pass(1, "student", "2026-01-01", "2026-06-30")

print("Before renewal:")
manager.display_passes()

manager.renew_pass(1, "2027-06-30")

print("\nAfter renewal:")
manager.display_passes()

print("\nAttempting to renew a non-existent bus pass:")
manager.renew_pass(99, "2027-06-30")
