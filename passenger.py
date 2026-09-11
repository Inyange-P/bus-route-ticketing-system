# Passenger model for the Bus Route and Ticket Management system

class Passenger:
    # Represents one registered passenger.
    def __init__(self, passenger_id, name, phone):
        self.passenger_id = passenger_id
        self.name = name
        self.phone = phone

    def __str__(self):
        # Return the passenger information in a readable format.
        return ( 
            f"Passenger(ID: {self.passenger_id} | "
            f"Name: {self.name} | " 
            f"Phone: {self.phone}"
        )
    