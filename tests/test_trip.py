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


    def test_seat_layout_populated_after_add_trip(self):
        # Seats only get filled in when created through TripManager.add_trip,
        # so we simulate that here directly on the Trip object
        trip = Trip("T003", "R001", "2026-09-15", "08:00", "12:00", 3)
        trip.seats = {1: True, 2: True, 3: True}

        layout = trip.view_seat_layout()
        self.assertIn("[1:O]", layout)
        self.assertIn("[2:O]", layout)
        self.assertIn("[3:O]", layout)

    def test_is_seat_available(self):
        trip = Trip("T004", "R001", "2026-09-15", "08:00", "12:00", 3)
        trip.seats = {1: True, 2: False, 3: True}

        self.assertTrue(trip.is_seat_available(1))
        self.assertFalse(trip.is_seat_available(2))

    def test_is_seat_available_invalid_seat(self):
        # Asking about a seat number that doesn't exist should return False, not crash
        trip = Trip("T005", "R001", "2026-09-15", "08:00", "12:00", 3)
        trip.seats = {1: True, 2: True, 3: True}

        self.assertFalse(trip.is_seat_available(99))

    def test_book_seat_success(self):
        trip = Trip("T006", "R001", "2026-09-15", "08:00", "12:00", 3)
        trip.seats = {1: True, 2: True, 3: True}

        result = trip.book_seat(1)
        self.assertTrue(result)
        self.assertFalse(trip.seats[1])  # seat 1 should now be booked

    def test_book_seat_already_booked(self):
        trip = Trip("T007", "R001", "2026-09-15", "08:00", "12:00", 3)
        trip.seats = {1: False, 2: True, 3: True}  # seat 1 already booked

        result = trip.book_seat(1)
        self.assertFalse(result)  # booking should fail


if __name__ == "__main__":
    unittest.main()
    