from bus_pass_manager import BusPassManager

manager = BusPassManager()

print("Issuing a valid bus pass")
p1 = manager.issue_pass(1, "student", "2026-01-01", "2027-01-01")
print(p1)

print("\nIssuing an invalid bus pass")
p2 = manager.issue_pass(2, "banana", "2026-01-01", "2027-01-01")
print(p2)

print("\nIssuing a bus pass with invalid date order")
p3 = manager.issue_pass(3, "senior", "2027-01-01", "2026-01-01")
print(p3)
    
manager.display_passes()