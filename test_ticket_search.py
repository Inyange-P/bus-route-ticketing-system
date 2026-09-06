# Tests for TicketManager.search_ticket

# search_ticket is meant to look up a single ticket by its ID. We test the normal case, the "not found" case, and every kind of bad input someone could accidentally pass in, so the rest of the system can trust
# that search_ticket either returns a real Ticket, returns None, or raises a clear error -- it should never crash in a confusing way.

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


def test_search_finds_existing_ticket():
# The normal case: searching for a ticket ID that exists should return that exact ticket object, with all of its details intact.
    manager = make_manager_with_one_ticket()

    result = manager.search_ticket(1)

    assert result is not None, "Expected to find ticket 1, but got None."
    assert result.ticket_id == 1
    assert result.passenger_id == 101
    assert result.trip_id == 1
    assert result.seat_number == 5
    assert result.price == 50
    print("PASS: search_ticket finds an existing ticket.")


def test_search_returns_none_for_missing_ticket():
# Searching for a ticket ID that was never added should return None, not raise an error. A "not found" result is a normal, expected outcome, not an exceptional one -- the staff member just tries a different ID.
    manager = make_manager_with_one_ticket()

    result = manager.search_ticket(999)

    assert result is None, "Expected None for a ticket ID that does not exist."
    print("PASS: search_ticket returns None for a non-existent ticket ID.")


def test_search_rejects_non_integer_types():
# A ticket ID must be a whole number. Strings, floats, None, and lists are all invalid and should raise TypeError immediately, rather than silently failing or crashing somewhere deeper in the lookup.
    manager = make_manager_with_one_ticket()

    invalid_values = ["1", 1.5, None, [1], {"id": 1}]

    for bad_value in invalid_values:
        try:
            manager.search_ticket(bad_value)
        except TypeError:
            continue
        else:
            raise AssertionError(
                f"Expected TypeError for ticket_id={bad_value!r}, "
                "but no error was raised."
            )

    print("PASS: search_ticket rejects every non-integer type with TypeError.")


def test_search_rejects_boolean_ticket_ids():
# In Python, bool is technically a subclass of int, so isinstance(True, int) is True. Without an explicit check, True/False could be mistaken for 1/0.
# A ticket ID of True or False makes no real-world sense, so both must be rejected with TypeError, exactly like any other non-integer input.
    manager = make_manager_with_one_ticket()

    for bad_value in (True, False):
        try:
            manager.search_ticket(bad_value)
        except TypeError:
            continue
        else:
            raise AssertionError(
                f"Expected TypeError for ticket_id={bad_value!r}, "
                "but it was silently accepted as an integer."
            )

    print("PASS: search_ticket rejects True and False as invalid ticket IDs.")


def test_search_rejects_zero_and_negative_ids():
# Ticket IDs are generated starting from 1 and only ever increase, so zero or negative numbers can never be real ticket IDs. These should raise ValueError, since the type is correct but the value is out of range.
    manager = make_manager_with_one_ticket()

    for bad_value in (0, -1, -100):
        try:
            manager.search_ticket(bad_value)
        except ValueError:
            continue
        else:
            raise AssertionError(
                f"Expected ValueError for ticket_id={bad_value!r}, "
                "but no error was raised."
            )

    print("PASS: search_ticket rejects zero and negative ticket IDs.")


def test_search_still_finds_cancelled_tickets():
# search_ticket looks up a ticket by ID only -- it should not care whether the ticket is active or cancelled. Hiding cancelled tickets is the job of
# display_active_tickets/display_cancelled_tickets, not search_ticket. A cancelled ticket must still be searchable, e.g. so staff can look up its details or confirm a refund.
    manager = make_manager_with_one_ticket()

    manager.cancel_ticket(1)
    result = manager.search_ticket(1)

    assert result is not None, "Expected to still find a cancelled ticket."
    assert result.status == "cancelled"
    print("PASS: search_ticket still finds a ticket after it has been cancelled.")


def run_all_tests():
    test_search_finds_existing_ticket()
    test_search_returns_none_for_missing_ticket()
    test_search_rejects_non_integer_types()
    test_search_rejects_boolean_ticket_ids()
    test_search_rejects_zero_and_negative_ids()
    test_search_still_finds_cancelled_tickets()
    print("\nAll search_ticket tests passed.")


if __name__ == "__main__":
    run_all_tests()