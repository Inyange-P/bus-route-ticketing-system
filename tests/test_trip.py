import unittest
from trip import Trip


class testTrip(unittest.TestCase):
    """"
    Tests for the Trip class.
    Checks that a trip Object stores its data correctly.
    """


    def test_trip_creation(self):
        # Create a Sample trip
        trip = Trip(
            trip_id="T001",
            route_id="R001",
            date="2026-09-12",
            departure_time="01:14",
            arrival_time="05:00",
            total_seats=40
        )

    #Check if each attribute ws created correctly
        self.assertEqual(trip.trip_id, "T001")
        self.assertEqual(trip.route_id, "R001")
        self.assertEqual(trip.date, "2026-09-12")
        self.assertEqual(trip.departure_time, "01:14")
        self.assertEqual(trip.arrival_time, "05:00")
        self.assertEqual(trip.total_seats, 40)

    #Seat dictionary should atart empty
        self.assertEqual(trip.seats, {})


def test_trip_str(self):
    #check thatprinting a trip includes its trip_id
    trip = Trip("T002", "R002", "2026-09-13", "02:00", "06:00", 50)
    self.assertIn("T002", str(trip))


if __name__ == "__main__":
    unittest.main()
    