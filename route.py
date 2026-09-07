#Route model for the Bus Route and Ticketing managment system

class Route:
    # Represents one bus route between an origin and a destination.

    def __init__(self, route_id, origin, destination, distance_km, base_fare):
        self.route_id = route_id
        self.origin = origin
        self.destination = destination
        self.distance_km = distance_km
        self.base_fare = base_fare

    def __str__(self):
        # Return the route information in a readable format.
        return (
            f"Route ID: {self.route_id} | "
            f"Origin: {self.origin} | "
            f"Destination: {self.destination} | "
            f"Distance: {self.distance_km} km | "
            f"Base Fare: ${self.base_fare:.2f}"
        )