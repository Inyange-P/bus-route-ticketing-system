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