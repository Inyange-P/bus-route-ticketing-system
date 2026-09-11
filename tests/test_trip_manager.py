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


if __name__ == "__main__":
    unittest.main()
    