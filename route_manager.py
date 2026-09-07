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
