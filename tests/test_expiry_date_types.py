from datetime import date, datetime
from bus_pass_manager import BusPassManager

manager = BusPassManager()

print("Issuing a pass with a real date object as expiry_date:")
manager.issue_pass(1, "student", date(2026, 1, 1), date(2026, 12, 31))

print("\nChecking validity with a text travel date:")
print(manager.is_pass_valid(1, "2026-06-15"))

print("\nChecking validity with a real date object as travel date:")
print(manager.is_pass_valid(1, date(2026, 6, 15)))

print("\nChecking an expired date:")
print(manager.is_pass_valid(1, date(2027, 1, 15)))