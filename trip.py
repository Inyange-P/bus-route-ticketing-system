class Trip: 
    #Represents a single bus trip. Stores trip details and tracks seat availability.
    def __init__(self, trip_id, route_id, date, departure_time, arrival_time, total_seats): # Unique identifier for this trip (e.g. "T001")
        self.trip_id =trip_id
        self.route_id = route_id
        self.date = date
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.total_seats = total_seats
        self.seats ={} # seat_number: True(availabe) / False (booked)

    def __str__(self): # Defines how a Trip object looks when printed.
        return (f"Trip {self.trip_id} | Route: {self.route_id} | "
                f"Date: {self.date} | Departure: {self.departure_time} | "
                f"Arrival: {self.arrival_time} | Seats: {self.total_seats}")


    def view_seat_layout(self):
        # Builds a readable string showing every seat and its status
        layout = ""

        for seat_number, is_available in self.seats.items():
            # O means open/available, X means booked
            status = "O" if is_available else "X"
            layout += f"[{seat_number}:{status}] "

        return layout.strip()


    def is_seat_available(self, seat_number):
        # Checks if a given seat number is free.
        # .get() looks up the seat safely — if the seat doesn't exist, it returns False instead of crashing
        return self.seats.get(seat_number, False)

    def book_seat(self, seat_number):
        # Only book the seat if it's actually available
        if self.is_seat_available(seat_number):
            self.seats[seat_number] = False
            return True

        # Seat was already booked or doesn't exist
        return False