from datetime import datetime
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

    def issue_pass(self, passenger_id, pass_type, issue_date, expiry_date):
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

    def is_pass_valid(self, pass_id, travel_date):
        # checks whether a bus pass can be used for a discount/free travel on the given date 
        if pass_id not in self.bus_passes:
            return False, "Bus pass not found."

        bus_pass = self.bus_passes[pass_id]

        if bus_pass.status != "active":
            return False, "Bus pass is not active."

        expiry_date = datetime.strptime(bus_pass.expiry_date, "%Y-%m-%d")
        travel_date = datetime.strptime(travel_date, "%Y-%m-%d")

        if travel_date > expiry_date:
            return False, "Bus pass has expired."

        return True, "Bus pass is valid."