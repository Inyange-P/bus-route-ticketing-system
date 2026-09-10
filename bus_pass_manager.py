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

