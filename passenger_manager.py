from passenger import Passenger

class PassengerManager:
    # Manages all passengers in the system.

    def __init__(self):
        self.passengers = {}

    def generate_passenger_id(self):
        # if there are no passengers yet start from ID 1.
        if not self.passengers:
            return 1
        # otherwise, continue from the highest existing passenger ID.
        return max(self.passengers.keys()) + 1

    def register_passenger(self, name, phone):
        passenger_id = self.generate_passenger_id()
        passenger = Passenger(passenger_id, name, phone)
        self.passengers[passenger_id] = passenger
        return passenger

    def search_passenger(self, passenger_id=None, name=None, phone=None):
        matches = []
        for passenger in self.passengers.values():
            if passenger_id is not None and passenger.passenger_id == passenger_id:
                matches.append(passenger)
            elif name is not None and passenger.name.lower() == name.lower():
                matches.append(passenger)
            elif phone is not None and passenger.phone == phone:
                matches.append(passenger)
        return matches

    def display_passengers(self):
        if not self.passengers:
            print("No passengers registered.")
            return
        print("\n----- REGISTERED PASSENGERS -----")
        for passenger in self.passengers.values():
            print(passenger)

    def update_passenger(self, passenger_id, name=None, phone=None):
        if passenger_id not in self.passengers:
            print(f"No passenger found with ID {passenger_id}.")
            return None
        passenger = self.passengers[passenger_id]
        if name is not None:
            passenger.name = name
        if phone is not None:
            passenger.phone = phone
        return passenger