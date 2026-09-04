#Ticket model for the Bus Route and Ticketing Management System.

from datetime import date
from typing import Optional


class Ticket:
#Represent a ticket purchased by a passenger for a bus trip.

    VALID_STATUSES = {"active", "cancelled"}

    def __init__(
        self,
        ticket_id: int,
        passenger_id: int,
        trip_id: int,
        seat_number: int,
        price: float,
        pass_id: Optional[int] = None,
        purchase_date: Optional[date] = None,
        status: str = "active",
    ):
#Create a new ticket.

#Args:
    #ticket_id: Unique identifier for the ticket.
    #passenger_id: ID of the passenger buying the ticket.
    #trip_id: ID of the bus trip.
    #seat_number: Seat selected by the passenger.
    #price: Final ticket price.
    #pass_id: ID of the bus pass used, if applicable.
    #purchase_date: Date the ticket was purchased.
    #status: Current ticket status.

#Raises:
    #ValueError: If any ticket information is invalid.
    
        self._validate_id(ticket_id, "ticket ID")
        self._validate_id(passenger_id, "passenger ID")
        self._validate_id(trip_id, "trip ID")
        self._validate_seat_number(seat_number)
        self._validate_price(price)
        self._validate_pass_id(pass_id)
        self._validate_status(status)

        self.ticket_id = ticket_id
        self.passenger_id = passenger_id
        self.trip_id = trip_id
        self.seat_number = seat_number
        self.pass_id = pass_id
        self.price = price
        self.purchase_date = purchase_date or date.today()
        self.status = status

    @staticmethod
    def _validate_id(value: int, field_name: str):
#Validate an ID used by the ticket.
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{field_name} must be an integer.")

        if value <= 0:
            raise ValueError(f"{field_name} must be greater than zero.")

    @staticmethod
    def _validate_seat_number(seat_number: int):
#Validate the ticket's seat number.
        if isinstance(seat_number, bool) or not isinstance(seat_number, int):
            raise ValueError("Seat number must be an integer.")

        if seat_number <= 0:
            raise ValueError("Seat number must be greater than zero.")

    @staticmethod
    def _validate_price(price: float):
#Validate the final ticket price.
        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise ValueError("Ticket price must be a number.")

        if price < 0:
            raise ValueError("Ticket price cannot be negative.")

    @staticmethod
    def _validate_pass_id(pass_id: Optional[int]):
#Validate the optional bus pass ID.
        if pass_id is None:
            return

        if isinstance(pass_id, bool) or not isinstance(pass_id, int):
            raise ValueError("Pass ID must be an integer.")

        if pass_id <= 0:
            raise ValueError("Pass ID must be greater than zero.")

    @classmethod
    def _validate_status(cls, status: str):
#Validate the ticket status.
        if not isinstance(status, str):
            raise ValueError("Ticket status must be a string.")

        if status not in cls.VALID_STATUSES:
            valid_statuses = ", ".join(sorted(cls.VALID_STATUSES))
            raise ValueError(
                f"Invalid ticket status. Choose one of: {valid_statuses}."
            )

    def cancel(self):
#Cancel the ticket.
#Raises:
#ValueError: If the ticket has already been cancelled.
        
        if self.status == "cancelled":
            raise ValueError("Ticket is already cancelled.")

        self.status = "cancelled"

    def is_active(self):
#Return True when the ticket is currently active.
        return self.status == "active"

    def __str__(self):
#Return a readable representation of the ticket.
        pass_information = (
            str(self.pass_id) if self.pass_id is not None else "None"
        )

        return (
            f"Ticket ID: {self.ticket_id} | "
            f"Passenger ID: {self.passenger_id} | "
            f"Trip ID: {self.trip_id} | "
            f"Seat: {self.seat_number} | "
            f"Pass ID: {pass_information} | "
            f"Price: {self.price:.2f} | "
            f"Purchase Date: {self.purchase_date} | "
            f"Status: {self.status}"
        )