from bus_pass_manager import BusPassManager

manager = BusPassManager()

print("Issuing first bus pass for passenger 1:")
pass1 = manager.issue_pass(1, "student", "2026-01-01", "2027-01-01")
manager.display_passes()

print("\nAttempting to issue a second active bus pass for passenger 1:")
pass2 = manager.issue_pass(1, "senior", "2026-01-01", "2027-01-01")
manager.display_passes()

print("\nIssuing a bus pass for a different passenger (2):")
pass3 = manager.issue_pass(2, "priority", "2026-01-01", "2027-01-01")
manager.display_passes()