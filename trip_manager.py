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


    def add_trip(self, route_id, date, departure_time, arrival_time, total_seats):

        # Get a new unique ID for this trip
        trip_id = self.generate_trip_id()

        # Create the actual Trip object using the Trip class
        new_trip = Trip(trip_id, route_id, date, departure_time, arrival_time, total_seats)

        # Build the seat dictionary: every seat from 1 to total_seats starts as available (True)
        new_trip.seats = {i: True for i in range(1, total_seats + 1)}

        # Save this trip into our list of all trips
        self.trips.append(new_trip)

        return new_trip

    def display_trips(self):
        # If there are no trips yet, say so instead of printing nothing
        if not self.trips:
            print("No trips available.")
            return

        # Otherwise, print each trip using Trip's __str__ method
        for trip in self.trips:
            print(trip)

    def search_trips(self, route_id=None, date=None):
        # Start with all trips, then narrow down based on what was given
        results = self.trips

        # If a route_id was provided, keep only trips matching that route
        if route_id:
            results = [t for t in results if t.route_id == route_id]

        # If a date was provided, keep only trips matching that date
        if date:
            results = [t for t in results if t.date == date]

        return results


    def update_trip(self, trip_id, date=None, departure_time=None, arrival_time=None):
        # Go through every trip looking for a matching ID
        for trip in self.trips:
            if trip.trip_id == trip_id:
                # Only update fields that were actually given a new value
                if date:
                    trip.date = date
                if departure_time:
                    trip.departure_time = departure_time
                if arrival_time:
                    trip.arrival_time = arrival_time

                return True

        # No trip with that ID was found
        return False


    def cancel_trip(self, trip_id):
        # Go through every trip looking for a matching ID
        for trip in self.trips:
            if trip.trip_id == trip_id:
                # Remove it from the list entirely
                self.trips.remove(trip)
                return True

        # No trip with that ID was found
        return False