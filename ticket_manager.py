from ticket import Ticket


class TicketManager:
# This class manages all tickets in the system. It stores tickets, searches for them, displays them and cancels them.

    def __init__(self):
# Store tickets using ticket ID as key. Example: {1: Ticket object,2: Ticket object}
        self.tickets = {}

    def add_ticket(self, ticket):
# Add a ticket into the system.

        if not isinstance(ticket, Ticket):
            raise TypeError("Only Ticket objects can be added.")

        if ticket.ticket_id in self.tickets:
            raise ValueError(
                f"Ticket ID {ticket.ticket_id} already exists."
            )

        self.tickets[ticket.ticket_id] = ticket

    def generate_next_ticket_id(self):
# Generate the next available ticket ID.

        if not self.tickets:
            return 1

        return max(self.tickets.keys()) + 1

    def search_ticket(self, ticket_id):
# Search for a ticket using its ID. Return the ticket if found.

        if not isinstance(ticket_id, int):
            raise TypeError("Ticket ID must be an integer.")

        if ticket_id <= 0:
            raise ValueError("Ticket ID must be greater than zero.")

        return self.tickets.get(ticket_id)

    def display_all_tickets(self):
# Show all tickets in the system.

        if not self.tickets:
            print("No tickets found.")
            return

        print("\n----- ALL TICKETS -----")

        for ticket in self.tickets.values():
            print(ticket)

    def display_active_tickets(self):
# Show only active tickets.

        found = False

        for ticket in self.tickets.values():
            if ticket.status == "active":
                print(ticket)
                found = True

        if not found:
            print("No active tickets found.")

    def display_cancelled_tickets(self):
# Show only cancelled tickets.

        found = False

        for ticket in self.tickets.values():
            if ticket.status == "cancelled":
                print(ticket)
                found = True

        if not found:
            print("No cancelled tickets found.")

    def cancel_ticket(self, ticket_id):
# Cancel a ticket. The ticket stays in the system but its status changes.

        ticket = self.search_ticket(ticket_id)

        if ticket is None:
            raise ValueError(
                f"Ticket ID {ticket_id} does not exist."
            )

        if ticket.status == "cancelled":
            raise ValueError(
                "This ticket is already cancelled."
            )

        ticket.cancel()

        print(
            f"Ticket {ticket_id} cancelled successfully."
        )

    def get_tickets_by_passenger(self, passenger_id):
# Return all tickets belonging to one passenger.

        if not isinstance(passenger_id, int):
            raise TypeError(
                "Passenger ID must be an integer."
            )

        if passenger_id <= 0:
            raise ValueError(
                "Passenger ID must be greater than zero."
            )

        passenger_tickets = []

        for ticket in self.tickets.values():
            if ticket.passenger_id == passenger_id:
                passenger_tickets.append(ticket)

        return passenger_tickets

    def get_tickets_by_trip(self, trip_id):
# Return all tickets for one trip.

        if not isinstance(trip_id, int):
            raise TypeError(
                "Trip ID must be an integer."
            )

        if trip_id <= 0:
            raise ValueError(
                "Trip ID must be greater than zero."
            )

        trip_tickets = []

        for ticket in self.tickets.values():
            if ticket.trip_id == trip_id:
                trip_tickets.append(ticket)

        return trip_tickets

    def seat_is_taken(self, trip_id, seat_number):
# Check whether a seat is already occupied.

        for ticket in self.tickets.values():

            if (
                ticket.trip_id == trip_id
                and ticket.seat_number == seat_number
                and ticket.status == "active"
            ):
                return True

        return False

    def count_active_tickets(self, trip_id):
# Count how many active tickets exist for a trip.

        count = 0

        for ticket in self.tickets.values():

            if (
                ticket.trip_id == trip_id
                and ticket.status == "active"
            ):
                count += 1

        return count