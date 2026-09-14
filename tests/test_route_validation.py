from route_manager import RouteManager

manager = RouteManager()

print("Adding a valid route:")
route = manager.add_route(
    "Pamplemousses",
    "Port Louis",
    17,
    40
)
print(route)

print("\nTrying to add a route with an empty origin:")
route = manager.add_route(
    "",
    "Bagatelle",
    12,
    30
)
print(route)

print("\nTrying to add a route with an empty destination:")
route = manager.add_route(
    "Port Louis",
    "",
    12,
    30
)
print(route)

print("\nTrying to add a route with invalid distance:")
route = manager.add_route(
    "Port Louis",
    "Bagatelle",
    -5,
    30
)
print(route)

print("\nTrying to add a route with negative fare:")
route = manager.add_route(
    "Port Louis",
    "Bagatelle",
    12,
    -10
)
print(route)

print("\nTrying to update a route with an invalid destination:")
updated_route = manager.update_route(
    route_id=1,
    destination=""
)
print(updated_route)

print("\nChecking that the original route was not changed:")
print(manager.routes[1])