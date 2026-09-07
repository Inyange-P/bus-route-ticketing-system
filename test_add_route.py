from route_manager import RouteManager

manager = RouteManager()

route1 = manager.add_route(
    "Pamplemousses",
    "Port Louis", 
    17,
    40
)

route2 = manager.add_route(
    "Port Louis",
    "Bagatelle",
    12,
    30
)

print("First route:")
print(route1)

print("Second route:")
print(route2)

print("\nAll routes stored:")
print(manager.routes)

print("\nNumber of routes:", len(manager.routes))
print("Next route ID:", manager.generate_route_id())