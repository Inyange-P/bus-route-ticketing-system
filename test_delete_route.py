from route_manager import RouteManager

manager = RouteManager()

manager.add_route(
    "Pamplemousses",
    "Port Louis",
    17,
    40
)

manager.add_route(
    "Port Louis",
    "Mahebourg",
    47,
    65
)

print("Before deletion:")
manager.display_routes()

result = manager.delete_route(1)

if result:
    print("\nRoute deleted successfully.")

print("\nAfter deletion:")
manager.display_routes()

print("\nTrying to delete a route that does not exist:")

result = manager.delete_route(99)

if not result:
    print("Route not found.")

print("\nTesting deletion of a route with an existing trip:")

class TestTrip:
    def __init__(self, trip_id, route_id):
        self.trip_id = trip_id
        self.route_id = route_id

trips = {
    1: TestTrip(1, 2)
}

try:
    manager.delete_route(2, trips)

except ValueError as error:
    print(error)