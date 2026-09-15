from utils.validation import validate_pass_type, validate_date_order, validate_status, parse_date, validate_passenger_exists
from datetime import datetime, date
from bus_pass import BusPass

class BusPassManager:
    # Manages bus passes in the Bus Route and Ticket Management system.

    def __init__(self):
        self.bus_passes = {}

    def generate_pass_id(self):
        # if there are no bus passes yet start from ID 1.
        if not self.bus_passes:
            return 1
        # otherwise, continue from the highest existing bus pass ID.
        return max(self.bus_passes.keys()) + 1

    def issue_pass(self, passenger_id, pass_type, issue_date, expiry_date, passengers=None):
        if passengers is None:
            print("Cannot issue a pass: passenger records are required.")
            return None
        if not validate_passenger_exists(passenger_id, passengers):
            return None
        if not validate_pass_type(pass_type):
            return None
        if not validate_date_order(issue_date, expiry_date):
            return None
        
        # a passenger cannot have more than one active pass of the same type at the same time.
        for bus_pass in self.bus_passes.values():
            if bus_pass.passenger_id == passenger_id and bus_pass.status == "active":
                print("Cannot issue a new pass. The passenger already has an active pass.")
                return None

        # If no active pass of the same type is found, create a new bus pass.
        pass_id = self.generate_pass_id()
        bus_pass = BusPass(pass_id, passenger_id, pass_type, issue_date, expiry_date)
        self.bus_passes[pass_id] = bus_pass
        return bus_pass

    def display_passes(self):
        if not self.bus_passes:
            print("No bus passes issued.")
            return
        print("\n----- BUS PASSES -----")
        for bus_pass in self.bus_passes.values():
            print(bus_pass)


    def search_pass(self, pass_id=None, passenger_id=None):
        matches = []
        for bus_pass in self.bus_passes.values():
            if pass_id is not None and bus_pass.pass_id == pass_id:
                matches.append(bus_pass)
            elif passenger_id is not None and bus_pass.passenger_id == passenger_id:
                matches.append(bus_pass)
        return matches

    def is_pass_valid(self, pass_id, travel_date, passenger_id=None):
        # Check status and both date boundaries; check ownership when supplied.
        if pass_id not in self.bus_passes:
            return False

        bus_pass = self.bus_passes[pass_id]
        if bus_pass.status != "active":
            return False
        if passenger_id is not None and bus_pass.passenger_id != passenger_id:
            return False

        try:
            issue_date = parse_date(bus_pass.issue_date)
            expiry_date = parse_date(bus_pass.expiry_date)
            travel_date = parse_date(travel_date)
        except ValueError:
            print("Invalid date format.")
            return False

        return issue_date <= travel_date <= expiry_date

    def renew_pass(self, pass_id, new_expiry_date):
        if pass_id not in self.bus_passes:
            print("Cannot renew: Bus pass does not exist.")
            return None

        bus_pass = self.bus_passes[pass_id]

        if not validate_date_order(bus_pass.issue_date, new_expiry_date):
            return None
        
        bus_pass.expiry_date = new_expiry_date
        bus_pass.status = "active"  # Reactivate the pass upon renewal
        return bus_pass

    def set_pass_status(self, pass_id, status):
        if not validate_status(status):
            print("Cannot update status: Invalid status.")
            return None

        # status should be "suspended" or "cancelled"
        if pass_id not in self.bus_passes:
            print("Cannot update status: Bus pass does not exist.")
            return None

        bus_pass = self.bus_passes[pass_id]
        bus_pass.status = status
        return bus_pass

    