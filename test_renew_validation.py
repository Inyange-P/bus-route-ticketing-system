from bus_pass_manager import BusPassManager

manager = BusPassManager()
manager.issue_pass(1, "student", "2026-01-01", "2027-07-01")

print("Trying to renew the bus pass with an expiry date that is before the issue date:")
result = manager.renew_pass(1, "2025-12-31")
print(result)

print("\nRenewng the bus pass with a valid expiry date:")
result = manager.renew_pass(1, "2028-01-01")
print(result)

manager.display_passes()
