from route_manager import RouteManager

manager = RouteManager()

print("Testing with no routes:")
manager.display_routes()

manager.add_route(
    "Pamplemousses",
    "Port Louis",
    17,
    40
)

manager.add_route(
    "Port Louis",
    "Bagatelle",
    10,
    30
)

print("\nTesting with routes:")
manager.display_routes()