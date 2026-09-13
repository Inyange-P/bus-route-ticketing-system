from trip import Trip


class TripManager:
    def __init__(self):
        self.trips = {}

    def generate_trip_id(self):
        if not self.trips:
            return 1
        return max(self.trips.keys()) + 1

    def add_trip(self, route_id, travel_date, departure_time, arrival_time, total_seats):
        trip_id = self.generate_trip_id()
        new_trip = Trip(trip_id, route_id, travel_date, departure_time, arrival_time, total_seats)
        self.trips[trip_id] = new_trip
        return new_trip

    def display_trips(self):
        if not self.trips:
            print("No trips available.")
            return
        for trip in self.trips.values():
            print(trip)

    def search_trips(self, route_id=None, travel_date=None):
        results = list(self.trips.values())
        if route_id is not None:
            results = [t for t in results if t.route_id == route_id]
        if travel_date is not None:
            results = [t for t in results if t.travel_date == travel_date]
        return results

    def update_trip(self, trip_id, travel_date=None, departure_time=None, arrival_time=None):
        if trip_id not in self.trips:
            return False

        trip = self.trips[trip_id]
        if travel_date is not None:
            trip.travel_date = travel_date
        if departure_time is not None:
            trip.departure_time = departure_time
        if arrival_time is not None:
            trip.arrival_time = arrival_time

        return True

    def cancel_trip(self, trip_id, ticket_manager=None):
        if trip_id not in self.trips:
            return False

        if ticket_manager is not None:
            if ticket_manager.count_active_tickets(trip_id) > 0:
                raise ValueError(
                    "Trip cannot be cancelled because it has active tickets."
                )

        del self.trips[trip_id]
        return True

    def is_seat_available(self, trip_id, seat_number, ticket_manager):
        # Delegates to Providence's seat_is_taken — TicketManager is now
        # the single source of truth for seat occupancy.
        if trip_id not in self.trips:
            return False
        return not ticket_manager.seat_is_taken(trip_id, seat_number)

    def view_seat_layout(self, trip_id, ticket_manager):
        # Builds the seat map by checking each seat against actual tickets,
        # instead of a separate flag stored on the Trip itself.
        if trip_id not in self.trips:
            return "Trip not found."

        trip = self.trips[trip_id]
        layout = ""

        for seat_number in range(1, trip.total_seats + 1):
            is_taken = ticket_manager.seat_is_taken(trip_id, seat_number)
            status = "X" if is_taken else "O"
            layout += f"[{seat_number}:{status}] "

        return layout.strip()