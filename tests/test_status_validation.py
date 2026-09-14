from bus_pass_manager import BusPassManager

manager = BusPassManager()

manager.issue_pass(1, "student", "2026-01-01", "2027-01-01")

print("Setting a valid status (suspended):")
result = manager.set_pass_status(1, "suspended")
print(result)

print("\nSetting an invalid status:")
result = manager.set_pass_status(1, "mango")
print(result)

manager.display_passes()
