# Tests for TicketManager.cancel_ticket

# cancel_ticket is meant to mark an active ticket as cancelled without deleting it from the system, and -- just as importantly -- to free up its seat so it can be sold to someone else on the same trip.
#
# We test the normal case, every kind of invalid input, the "already cancelled" guard, and the seat-release behaviour that the project requirements explicitly call for (Scenario E: cancel a ticket, then the seat becomes available again).

from datetime import date

from ticket import Ticket
from ticket_manager import TicketManager


def make_manager_with_one_ticket():
# Helper: build a fresh manager with exactly one active ticket in it, so every test starts from the same known state instead of repeating setup.
    manager = TicketManager()

    ticket = Ticket(
        ticket_id=1,
        passenger_id=101,
        trip_id=1,
        seat_number=5,
        price=50,
    )

    manager.add_ticket(ticket)
    return manager


class FakeRoute:
# A minimal stand-in for Abigail's Route class, just enough for purchase_ticket to read base_fare from it.
    def __init__(self):
        self.route_id = 1
        self.base_fare = 50.00


class FakeTrip:
# A minimal stand-in for Moses's Trip class, just enough for purchase_ticket to validate it and read its total_seats.
    def __init__(self):
        self.trip_id = 1
        self.route_id = 1
        self.travel_date = date(2026, 9, 10)
        self.total_seats = 40


class FakePassenger:
# A minimal stand-in for Chinelo's Passenger class, just enough for purchase_ticket to confirm the passenger exists.
    def __init__(self, passenger_id):
        self.passenger_id = passenger_id


def test_cancel_marks_active_ticket_as_cancelled():
# The normal case: cancelling an active ticket should flip its status to "cancelled" without deleting it or changing any other field.
    manager = make_manager_with_one_ticket()

    manager.cancel_ticket(1)
    ticket = manager.search_ticket(1)

    assert ticket is not None, "Cancelling a ticket must not remove it from the system."
    assert ticket.status == "cancelled"
# Everything else about the ticket should stay exactly as it was.
    assert ticket.passenger_id == 101
    assert ticket.trip_id == 1
    assert ticket.seat_number == 5
    assert ticket.price == 50
    print("PASS: cancel_ticket marks an active ticket as cancelled and leaves other fields untouched.")


def test_cancel_raises_for_missing_ticket():
# Trying to cancel a ticket ID that was never added should raise ValueError with a clear message, not crash or silently do nothing.
    manager = make_manager_with_one_ticket()

    try:
        manager.cancel_ticket(999)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError when cancelling a ticket that does not exist.")

    print("PASS: cancel_ticket raises ValueError for a ticket ID that does not exist.")


def test_cancel_raises_for_already_cancelled_ticket():
# Cancelling the same ticket twice should not be allowed. The second attempt must raise ValueError instead of pretending to succeed again.
    manager = make_manager_with_one_ticket()

    manager.cancel_ticket(1)

    try:
        manager.cancel_ticket(1)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError when cancelling an already-cancelled ticket.")

    print("PASS: cancel_ticket raises ValueError when the ticket is already cancelled.")


def test_cancel_rejects_invalid_ticket_id_types():
# cancel_ticket calls search_ticket internally, so it should inherit the same strict type checking: non-integers raise TypeError, and booleans (which Python treats as a subclass of int) must not slip through as 1/0.
    manager = make_manager_with_one_ticket()

    invalid_values = ["1", 1.5, None, True, False]

    for bad_value in invalid_values:
        try:
            manager.cancel_ticket(bad_value)
        except TypeError:
            continue
        else:
            raise AssertionError(
                f"Expected TypeError for ticket_id={bad_value!r}, "
                "but no error was raised."
            )

    print("PASS: cancel_ticket rejects non-integer and boolean ticket IDs with TypeError.")


def test_cancel_rejects_zero_and_negative_ids():
# Ticket IDs are always positive, so zero or negative values are out of range rather than the wrong type, and should raise ValueError.
    manager = make_manager_with_one_ticket()

    for bad_value in (0, -1, -50):
        try:
            manager.cancel_ticket(bad_value)
        except ValueError:
            continue
        else:
            raise AssertionError(
                f"Expected ValueError for ticket_id={bad_value!r}, "
                "but no error was raised."
            )

    print("PASS: cancel_ticket rejects zero and negative ticket IDs with ValueError.")


def test_cancel_frees_the_seat_for_repurchase():
# This is the behaviour the project spec explicitly requires (Scenario E): cancelling a ticket must make its seat available again, so another passenger can be sold that same seat on the same trip.
    manager = TicketManager()
    routes = {1: FakeRoute()}
    trips = {1: FakeTrip()}
    passengers = {101: FakePassenger(101), 102: FakePassenger(102)}

    first_ticket = manager.purchase_ticket(
        passenger_id=101,
        trip_id=1,
        seat_number=10,
        routes=routes,
        passengers=passengers,
        trips=trips,
    )

# Before cancelling, the seat should be reported as taken, and a second passenger should not be able to buy the same seat.
    assert manager.seat_is_taken(1, 10) is True

    try:
        manager.purchase_ticket(
            passenger_id=102,
            trip_id=1,
            seat_number=10,
            routes=routes,
            passengers=passengers,
            trips=trips,
        )
    except ValueError:
        pass
    else:
        raise AssertionError("Expected the second purchase on the same seat to be rejected.")

# Cancel the first ticket. The seat must now be free.
    manager.cancel_ticket(first_ticket.ticket_id)
    assert manager.seat_is_taken(1, 10) is False, "Seat should be free again after cancellation."

# A different passenger should now be able to buy that exact seat.
    second_ticket = manager.purchase_ticket(
        passenger_id=102,
        trip_id=1,
        seat_number=10,
        routes=routes,
        passengers=passengers,
        trips=trips,
    )

    assert second_ticket.seat_number == 10
    assert second_ticket.passenger_id == 102
    assert second_ticket.status == "active"

    print("PASS: cancel_ticket frees the seat so it can be sold to another passenger.")


def test_cancel_does_not_affect_other_tickets_on_same_trip():
# Cancelling one ticket should only affect that ticket. Other active tickets on the very same trip must remain untouched.
    manager = TicketManager()
    routes = {1: FakeRoute()}
    trips = {1: FakeTrip()}
    passengers = {101: FakePassenger(101), 102: FakePassenger(102)}

    ticket_a = manager.purchase_ticket(
        passenger_id=101, trip_id=1, seat_number=1,
        routes=routes, passengers=passengers, trips=trips,
    )
    ticket_b = manager.purchase_ticket(
        passenger_id=102, trip_id=1, seat_number=2,
        routes=routes, passengers=passengers, trips=trips,
    )

    manager.cancel_ticket(ticket_a.ticket_id)

    untouched = manager.search_ticket(ticket_b.ticket_id)
    assert untouched.status == "active", "Cancelling one ticket must not affect a different ticket."
    assert manager.seat_is_taken(1, 2) is True, "Seat 2 should still be taken by ticket_b."

    print("PASS: cancel_ticket only affects the targeted ticket, not other tickets on the same trip.")


def run_all_tests():
    test_cancel_marks_active_ticket_as_cancelled()
    test_cancel_raises_for_missing_ticket()
    test_cancel_raises_for_already_cancelled_ticket()
    test_cancel_rejects_invalid_ticket_id_types()
    test_cancel_rejects_zero_and_negative_ids()
    test_cancel_frees_the_seat_for_repurchase()
    test_cancel_does_not_affect_other_tickets_on_same_trip()
    print("\nAll cancel_ticket tests passed.")


if __name__ == "__main__":
    run_all_tests()