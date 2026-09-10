# BusPass model for the Bus Route and Ticket Management system

class BusPass:
    # Represents one bus pass issued to a single passenger. 

    def __init__(self, pass_id, passenger_id, pass_type, issue_date, expiry_date, status="active"):
        self.pass_id = pass_id
        self.passenger_id = passenger_id
        self.pass_type = pass_type
        self.issue_date = issue_date
        self.expiry_date = expiry_date
        self.status = status

    def __str__(self):
        # Return the bus pass information in a readable format.
        return(
            f"BusPass ID: {self.pass_id} | "
            f"Passenger ID: {self.passenger_id} | "
            f"Type: {self.pass_type} | "
            f"Issue Date: {self.issue_date} | "
            f"Expiry Date: {self.expiry_date} | "
            f"Status: {self.status}"
        )
        
