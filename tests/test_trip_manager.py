import unittest
from datetime import date
from trip_manager import TripManager


class FakeTicketManager:
    """
    A stand-in for Providence's TicketManager, used only for testing.
    Lets us control exactly which seats are "taken" without needing
    real Ticket objects or her full purchase logic.
    """

    def __init__(self, taken_seats=None):
        # taken_seats: a set of (trip_id, seat_number) tuples
        self.taken_seats = taken_seats or set()

    def seat_is_taken(self, trip_id, seat_number):
        return (trip_id, seat_number) in self.taken_seats

    def count_active_tickets(self, trip_id):
        return len([s for (t, s) in self.taken_seats if t == trip_id])


class TestTripManager(unittest.TestCase):

    def setUp(self):
        self.manager = TripManager()

    def test_manager_starts_empty(self):
        self.assertEqual(self.manager.trips, {})

    def test_generate_first_trip_id(self):
        trip_id = self.manager.generate_trip_id()
        self.assertEqual(trip_id, 1)

    def test_generate_trip_id_increments(self):
        self.manager.add_trip(1, date(2026, 9, 15), "08:00", "12:00", 20)
        next_id = self.manager.generate_trip_id()
        self.assertEqual(next_id, 2)

    def test_add_trip(self):
        trip = self.manager.add_trip(1, date(2026, 9, 15), "08:00", "12:00", 20)
        self.assertEqual(len(self.manager.trips), 1)
        self.assertEqual(trip.route_id, 1)
        self.assertEqual(trip.trip_id, 1)

    def test_add_multiple_trips(self):
        self.manager.add_trip(1, date(2026, 9, 15), "08:00", "12:00", 20)
        self.manager.add_trip(2, date(2026, 9, 16), "09:00", "13:00", 15)
        self.assertEqual(len(self.manager.trips), 2)

    def test_search_by_route(self):
        self.manager.add_trip(1, date(2026, 9, 15), "08:00", "12:00", 20)
        self.manager.add_trip(2, date(2026, 9, 16), "09:00", "13:00", 15)

        results = self.manager.search_trips(route_id=1)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].route_id, 1)

    def test_search_by_date(self):
        self.manager.add_trip(1, date(2026, 9, 15), "08:00", "12:00", 20)
        self.manager.add_trip(2, date(2026, 9, 16), "09:00", "13:00", 15)

        results = self.manager.search_trips(travel_date=date(2026, 9, 16))
        self.assertEqual(len(results), 1)

    def test_search_with_no_filters_returns_all(self):
        self.manager.add_trip(1, date(2026, 9, 15), "08:00", "12:00", 20)
        self.manager.add_trip(2, date(2026, 9, 16), "09:00", "13:00", 15)

        results = self.manager.search_trips()
        self.assertEqual(len(results), 2)

    def test_update_trip(self):
        trip = self.manager.add_trip(1, date(2026, 9, 15), "08:00", "12:00", 20)
        self.manager.update_trip(trip.trip_id, travel_date=date(2026, 9, 20))
        self.assertEqual(trip.travel_date, date(2026, 9, 20))

    def test_update_trip_not_found(self):
        result = self.manager.update_trip(999, travel_date=date(2026, 9, 20))
        self.assertFalse(result)

    def test_cancel_trip_no_ticket_manager(self):
        trip = self.manager.add_trip(1, date(2026, 9, 15), "08:00", "12:00", 20)
        result = self.manager.cancel_trip(trip.trip_id)
        self.assertTrue(result)
        self.assertEqual(len(self.manager.trips), 0)

    def test_cancel_trip_blocked_by_active_tickets(self):
        trip = self.manager.add_trip(1, date(2026, 9, 15), "08:00", "12:00", 20)

        # Simulate seat 1 on this trip being booked
        fake_tm = FakeTicketManager(taken_seats={(trip.trip_id, 1)})

        with self.assertRaises(ValueError):
            self.manager.cancel_trip(trip.trip_id, ticket_manager=fake_tm)

        # Trip should still exist since cancellation was blocked
        self.assertIn(trip.trip_id, self.manager.trips)

    def test_cancel_trip_allowed_with_no_active_tickets(self):
        trip = self.manager.add_trip(1, date(2026, 9, 15), "08:00", "12:00", 20)
        fake_tm = FakeTicketManager()  # no taken seats

        result = self.manager.cancel_trip(trip.trip_id, ticket_manager=fake_tm)
        self.assertTrue(result)

    def test_is_seat_available_true(self):
        trip = self.manager.add_trip(1, date(2026, 9, 15), "08:00", "12:00", 20)
        fake_tm = FakeTicketManager()  # nothing taken

        self.assertTrue(self.manager.is_seat_available(trip.trip_id, 5, fake_tm))

    def test_is_seat_available_false_when_taken(self):
        trip = self.manager.add_trip(1, date(2026, 9, 15), "08:00", "12:00", 20)
        fake_tm = FakeTicketManager(taken_seats={(trip.trip_id, 5)})

        self.assertFalse(self.manager.is_seat_available(trip.trip_id, 5, fake_tm))

    def test_view_seat_layout(self):
        trip = self.manager.add_trip(1, date(2026, 9, 15), "08:00", "12:00", 3)
        fake_tm = FakeTicketManager(taken_seats={(trip.trip_id, 2)})

        layout = self.manager.view_seat_layout(trip.trip_id, fake_tm)
        self.assertIn("[1:O]", layout)
        self.assertIn("[2:X]", layout)
        self.assertIn("[3:O]", layout)


if __name__ == "__main__":
    unittest.main()