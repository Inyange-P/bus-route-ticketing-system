from datetime import date, datetime
import math

from ticket import Ticket


class TicketManager:
# This class manages all tickets in the system. It stores tickets, searches for them, displays them and cancels them.

# These are the pass types supported by our system.
    VALID_PASS_TYPES = {"student", "senior", "priority"}

# The project says students get a reduced fare. Our written requirements do not give the exact percentage, so the team can change this one value after agreeing on it.
    STUDENT_DISCOUNT_RATE = 0.50
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
    def calculate_ticket_price(self, base_fare, pass_type=None):
# Start with the normal route fare. If there is no valid pass, the passenger pays the full fare.

        if isinstance(base_fare, bool) or not isinstance( base_fare, (int, float) ):
            raise TypeError("Base fare must be a number.")

        if not math.isfinite(float(base_fare)):
            raise ValueError( "Base fare must be a valid finite number." )

        if base_fare < 0:
            raise ValueError("Base fare cannot be negative.")

        if pass_type is None:
            return round(float(base_fare), 2)

        if not isinstance(pass_type, str):
            raise TypeError("Pass type must be text.")

        pass_type = pass_type.strip().lower()

        if not pass_type:
            raise ValueError("Pass type cannot be empty.")

    # Senior and priority passengers travel for free, when they have a valid pass.
        if pass_type in {"senior", "priority"}:
            return 0.00

        if pass_type == "student":
            discount = self.STUDENT_DISCOUNT_RATE

            if not 0 <= discount < 1:
              raise ValueError( "Student discount rate must be between 0 and 1." )

            return round(
              float(base_fare) * (1 - discount), 2 )
        raise ValueError( f"Unsupported pass type: {pass_type}." )

    def search_ticket(self, ticket_id):
# Search for a ticket using its ID. Return the ticket if found.

# In Python, bool is technically a subclass of int, so isinstance(True, int) is True.  Without this extra check, someone could accidentally search using True/False and it would silently be treated as 1/0 instead of being rejected as invalid input.
     if isinstance(ticket_id, bool) or not isinstance(ticket_id, int):
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
    def _validate_passenger(self, passenger_id, passengers):
# A ticket cannot be issued to a passenger, who is not registered in the system.

        if isinstance(passenger_id, bool) or not isinstance( passenger_id, int ):
            raise TypeError("Passenger ID must be an integer.")

        if passenger_id <= 0:
            raise ValueError( "Passenger ID must be greater than zero." )

        if passengers is None:
            raise ValueError( "Passenger information is not available." )

        if not hasattr(passengers, "get"):
            raise TypeError( "Passenger records must support ID lookup." )

        passenger = passengers.get(passenger_id)

        if passenger is None:
            raise ValueError( f"Passenger ID {passenger_id} does not exist." )

        return passenger
    def _validate_trip(self, trip_id, trips):
# The selected trip must exist before a ticket can be sold.

        if isinstance(trip_id, bool) or not isinstance( trip_id, int ):
            raise TypeError("Trip ID must be an integer.")

        if trip_id <= 0:
            raise ValueError( "Trip ID must be greater than zero." )

        if trips is None:
            raise ValueError( "Trip information is not available." )

        if not hasattr(trips, "get"):
            raise TypeError( "Trip records must support ID lookup." )

        trip = trips.get(trip_id)

        if trip is None:
            raise ValueError( f"Trip ID {trip_id} does not exist." )

        return trip

    def _validate_trip_information(self, trip):
# The ticket system depends on these values from Trip. Check them before using them so bad trip data does not cause confusing errors later.

        if not hasattr(trip, "route_id"):
            raise AttributeError( "Trip is missing route_id." )

        if not isinstance(trip.route_id, int) or isinstance( trip.route_id, bool ):
            raise TypeError( "Trip route_id must be an integer." )

        if trip.route_id <= 0:
            raise ValueError( "Trip route_id must be greater than zero." )

        if not hasattr(trip, "travel_date"):
            raise AttributeError( "Trip is missing travel_date." )

        if not isinstance(trip.travel_date, date):
            raise TypeError( "Trip travel_date must be a date." )

        if not hasattr(trip, "total_seats"):
            raise AttributeError( "Trip is missing total_seats." )

        if (
            isinstance(trip.total_seats, bool)
            or not isinstance(trip.total_seats, int)
        ):
            raise TypeError( "Trip total_seats must be an integer." )

        if trip.total_seats <= 0:
            raise ValueError( "Trip must have at least one seat." )

    def _get_route_for_trip(self, trip, routes):
# The trip tells us which route it belongs to. We need the route to get the base fare.

        if routes is None:
            raise ValueError( "Route information is not available." )

        if not hasattr(routes, "get"):
            raise TypeError( "Route records must support ID lookup." )

        route = routes.get(trip.route_id)

        if route is None:
            raise ValueError( f"Route ID {trip.route_id} does not exist." )

        if not hasattr(route, "base_fare"):
            raise AttributeError( "Route is missing base_fare." )

        return route

    def _validate_seat_for_purchase( self, trip_id, seat_number, trip ):
# A seat number must be a real positive whole number.

        if isinstance(seat_number, bool) or not isinstance( seat_number, int ):
            raise TypeError( "Seat number must be an integer." )

        if seat_number <= 0:
            raise ValueError( "Seat number must be greater than zero." )

        total_seats = trip.total_seats

# The seat must actually exist on this bus.
        if seat_number > total_seats:
            raise ValueError(
                f"Seat {seat_number} does not exist. "
                f"Choose a seat from 1 to {total_seats}." )

# Only active tickets occupy seats. A cancelled ticket should free its old seat.
        if self.seat_is_taken(trip_id, seat_number):
            raise ValueError( f"Seat {seat_number} is already occupied." )

# This protects against corrupted data where the number of active tickets has somehow reached the bus capacity.
        active_tickets = self.count_active_tickets(trip_id)

        if active_tickets >= total_seats:
            raise ValueError( "This trip is full. No seats are available." )

    def _get_pass_for_purchase( self, passenger_id, pass_id, passes, travel_date ):
# A passenger does not have to use a bus pass.
        if pass_id is None:
            return None

        if isinstance(pass_id, bool) or not isinstance( pass_id, int ):
            raise TypeError( "Pass ID must be an integer." )

        if pass_id <= 0:
            raise ValueError( "Pass ID must be greater than zero." )

        if passes is None:
            raise ValueError( "Bus pass information is not available." ) 

        if not hasattr(passes, "get"):
            raise TypeError( "Bus pass records must support ID lookup." )

        bus_pass = passes.get(pass_id)

        if bus_pass is None:
            raise ValueError( f"Pass ID {pass_id} does not exist." )

        if not hasattr(bus_pass, "passenger_id"):
            raise AttributeError( "Bus pass is missing passenger_id." )

# A passenger must not be able to use another passenger's personalised pass.
        if bus_pass.passenger_id != passenger_id:
            raise ValueError( "This bus pass does not belong to this passenger." )

        if not hasattr(bus_pass, "pass_type"):
            raise AttributeError("Bus pass is missing pass_type." )

        pass_type = bus_pass.pass_type

        if not isinstance(pass_type, str):
            raise TypeError( "Bus pass type must be text.")

        pass_type = pass_type.strip().lower()

        if pass_type not in self.VALID_PASS_TYPES:
            raise ValueError( f"Unsupported bus pass type: {pass_type}." )

        if not hasattr(bus_pass, "status"):
            raise AttributeError( "Bus pass is missing status."  )

        status = str(bus_pass.status).strip().lower()

# According to our project requirements, an inactive pass does not give the passenger a discount. The passenger can still buy the ticket at the normal fare.
        if status != "active":
            return None

        if not hasattr(bus_pass, "expiry_date"):
            raise AttributeError( "Bus pass is missing expiry_date." )

        expiry_date = bus_pass.expiry_date

        if not isinstance(expiry_date, date):
            raise TypeError( "Bus pass expiry_date must be a date." )

# An expired pass does not give a discount. The ticket can still be purchased at the normal fare.
        if travel_date > expiry_date:
            return None

# The pass is valid for this trip.
        return bus_pass

    def purchase_ticket(self, passenger_id, trip_id, seat_number, routes, passengers, trips, passes=None, pass_id=None ):
# Validate the passenger before doing anything else.
        self._validate_passenger( passenger_id, passengers )

# Validate the trip and its required information.
        trip = self._validate_trip( trip_id, trips )

        self._validate_trip_information(trip)

# Make sure the selected seat is valid and available.
        self._validate_seat_for_purchase( trip_id, seat_number, trip )

# Find the route connected to this trip.
        route = self._get_route_for_trip( trip, routes)

# Get the normal route fare.
        base_fare = route.base_fare

# Check the passenger's pass.
        valid_pass = self._get_pass_for_purchase( passenger_id, pass_id, passes, trip.travel_date )

        if valid_pass is None:
# No valid pass was used, so the passenger pays the normal route fare. 
            final_price = self.calculate_ticket_price( base_fare  )
            used_pass_id = None
        else:
# The pass is valid, so apply its fare rule.
            final_price = self.calculate_ticket_price( base_fare, valid_pass.pass_type )

            if not hasattr(valid_pass, "pass_id"):
             raise AttributeError( "Bus pass is missing pass_id." )
            used_pass_id = valid_pass.pass_id

# Generate the ID only after all validation has succeeded. This means failed purchases do not create unnecessary IDs.
        ticket_id = self.generate_next_ticket_id()

# Create the ticket only after every important check passed.
        ticket = Ticket( ticket_id=ticket_id, passenger_id=passenger_id, trip_id=trip_id, seat_number=seat_number, pass_id=used_pass_id, price=final_price )

# Store the completed ticket as the final step.
        self.add_ticket(ticket)

        return ticket

   