from datetime import date


class Trip:
    def __init__(self, trip_id, route_id, travel_date, departure_time, arrival_time, total_seats):
        self.trip_id = trip_id
        self.route_id = route_id
        self.travel_date = travel_date
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.total_seats = total_seats

        # No self.seats dict anymore — seat occupancy now lives in
        # TicketManager, checked via seat_is_taken(). This avoids having
        # two separate systems disagree about which seats are booked.

    def __str__(self):
        return (f"Trip {self.trip_id} | Route: {self.route_id} | "
                f"Date: {self.travel_date} | Departure: {self.departure_time} | "
                f"Arrival: {self.arrival_time} | Seats: {self.total_seats}")