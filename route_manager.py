from route import Route

class RouteManager:
    #Manages all routes in the system. 

    def __init__(self):
        self.routes = {}

    def generate_route_id(self):
        #if there are no routes yet start from ID 1.
        if not self.routes:
            return 1

        #otherwise, continue from the highest existing route ID.
        return max(self.routes.keys()) + 1

    def add_route(self, origin, destination, distance_km, base_fare):
        # Generate a new ID for the route.
        route_id = self.generate_route_id()

        # Create a new Route object.
        route = Route(
            route_id,
            origin,
            destination,
            distance_km,
            base_fare
        )

        #store the route using its ID.
        self.routes[route_id] = route

        return route

    def display_routes(self):
        # check i there are any routes to display
        if not self.routes:
            print("No routes available.")
            return

        print("\n----- AVAILABLE ROUTES -----")
        for route in self.routes.values():
            print(route)

    def search_routes(self, destination):
        # store any routes that match the destination
        matches = []

        for route in self.routes.values():
            if route.destination.lower() == destination.lower():
                matches.append(route)

        return matches