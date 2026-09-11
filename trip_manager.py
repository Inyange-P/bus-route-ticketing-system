from trip import Trip
# Import the Trip class so TripManager can create Trip objects


class TripManager:
    """
    Manages all trips in the system.
    Handles creating, storing, and generating IDs for trips.
    """

    def __init__(self):
        # A list to hold every Trip object that gets created
        self.trips = []

        # Used to generate the next trip ID (T001, T002, ...)
        self.next_id = 1

    def generate_trip_id(self):
        # Builds an ID like "T001", "T002", etc.
        # :03d means "pad the number with zeros to 3 digits"
        trip_id = f"T{self.next_id:03d}"

        # Increase the counter so the next trip gets a new ID
        self.next_id += 1

        return trip_id