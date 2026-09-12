import unittest
from trip_manager import TripManager


class TestTripManager(unittest.TestCase):
    """
    Tests for the TripManager class.
    Checks that it starts up correctly and generates trip IDs properly.
    """

    def setUp(self):
        # This runs automatically before every test below.
        # Creates a fresh TripManager so each test starts clean.
        self.manager = TripManager()

    def test_manager_starts_empty(self):
        # A brand new manager should have no trips yet
        self.assertEqual(self.manager.trips, [])

    def test_generate_first_trip_id(self):
        # The very first ID generated should be "T001"
        trip_id = self.manager.generate_trip_id()
        self.assertEqual(trip_id, "T001")

    def test_generate_trip_id_increments(self):
        # Each call should give a new, increasing ID
        first_id = self.manager.generate_trip_id()
        second_id = self.manager.generate_trip_id()
        third_id = self.manager.generate_trip_id()

        self.assertEqual(first_id, "T001")
        self.assertEqual(second_id, "T002")
        self.assertEqual(third_id, "T003")

    def test_add_trip(self):
        # Add one trip and confirm it was stored
        trip = self.manager.add_trip("R001", "2026-09-15", "08:00", "12:00", 20)

        self.assertEqual(len(self.manager.trips), 1)
        self.assertEqual(trip.route_id, "R001")
        self.assertEqual(trip.total_seats, 20)

    def test_add_trip_creates_seats(self):
        # The seats dictionary should have one entry per seat, all set to True
        trip = self.manager.add_trip("R001", "2026-09-15", "08:00", "12:00", 5)

        self.assertEqual(len(trip.seats), 5)
        self.assertTrue(all(trip.seats.values()))  # every seat should be available

    def test_add_multiple_trips(self):
        # Adding several trips should keep them all in the list
        self.manager.add_trip("R001", "2026-09-15", "08:00", "12:00", 20)
        self.manager.add_trip("R002", "2026-09-16", "09:00", "13:00", 15)

        self.assertEqual(len(self.manager.trips), 2)


if __name__ == "__main__":
    unittest.main()
