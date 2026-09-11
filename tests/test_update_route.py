from route_manager import RouteManager

manager = RouteManager()

route = manager.add_route(
    "Pamplemousses",
    "Port Louis",
    17,
    40
)
print("Before update:")
print(route)

updated_route = manager.update_route(
    route_id=1,
    base_fare=45
)

print("\nAfter changing fare:")
print(updated_route)

updated_route = manager.update_route(
    route_id=1,
    destination="Grand Baie",
    distance_km=20
)
print("\nAfter changing destination and distance:")
print(updated_route)

print("\nTrying to update a route that does not exist:")

result = manager.update_route(
    route_id=99,
    base_fare=100
)
if result is None:
    print("No route found.")