from datetime import datetime, date
from bus_pass_manager import BusPassManager

manager = BusPassManager()
manager.issue_pass(1, "student", "2026-01-01", "2027-01-01")

print("Checking validity with a text date:")
print(manager.is_pass_valid(1, "2026-06-01"))

print("\nChecking validity with a real date object:")
print(manager.is_pass_valid(1, datetime(2026, 6, 15, 14, 30)))

print("\nChecking validity with a datetime object:")
print(manager.is_pass_valid(1, datetime(2026, 6, 15, 14, 30)))

print("\nChecking an expired date object:")
print(manager.is_pass_valid(1, date(2027, 2, 1)))
