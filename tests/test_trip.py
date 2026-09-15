import unittest
from datetime import date
from trip import Trip


class TestTrip(unittest.TestCase):
    """
    Tests for the Trip class.
    Trip no longer tracks seats itself — just basic trip data.
    """

    def test_trip_creation(self):
        trip = Trip(
            trip_id=1,
            route_id=1,
            travel_date=date(2026, 9, 15),
            departure_time="08:00",
            arrival_time="12:00",
            total_seats=20
        )

        self.assertEqual(trip.trip_id, 1)
        self.assertEqual(trip.route_id, 1)
        self.assertEqual(trip.travel_date, date(2026, 9, 15))
        self.assertEqual(trip.departure_time, "08:00")
        self.assertEqual(trip.arrival_time, "12:00")
        self.assertEqual(trip.total_seats, 20)

    def test_trip_string_output(self):
        trip = Trip(2, 1, date(2026, 9, 16), "09:00", "13:00", 15)
        self.assertIn("Trip 2", str(trip))


if __name__ == "__main__":
    unittest.main()