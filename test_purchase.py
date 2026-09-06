from datetime import date

from ticket_manager import TicketManager


class TestRoute:
    def __init__(self):
        self.route_id = 1
        self.base_fare = 50.00


class TestTrip:
    def __init__(self):
        self.trip_id = 1
        self.route_id = 1
        self.travel_date = date(2026, 9, 10)
        self.total_seats = 40


class TestPassenger:
    def __init__(self):
        self.passenger_id = 101


manager = TicketManager()

routes = {
    1: TestRoute()
}

trips = {
    1: TestTrip()
}

passengers = {
    101: TestPassenger()
}

ticket = manager.purchase_ticket(
    passenger_id=101,
    trip_id=1,
    seat_number=10,
    routes=routes,
    passengers=passengers,
    trips=trips
)
ticket = manager.purchase_ticket(
    passenger_id=101,
    trip_id=1,
    seat_number=12,
    routes=routes,
    passengers=passengers,
    trips=trips
)
class TestStudentPass:
    def __init__(self):
        self.pass_id = 1
        self.passenger_id = 999
        self.pass_type = "student"
        self.status = "active"
        self.expiry_date = date(2026, 1, 1)
passes = {
        1: TestStudentPass()
}
ticket = manager.purchase_ticket(
    passenger_id=101,
    trip_id=1,
    seat_number=11,
    routes=routes,
    passengers=passengers,
    trips=trips,
    passes=passes,
    pass_id=1
)

print(ticket)


print("\nTicket purchased successfully:")
print(ticket)