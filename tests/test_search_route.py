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
    "Bagatelle",
    10,
    30
)

manager.add_route(
    "Bagatelle",
    "Quatre Bornes",
    6.2,
    15
)

print("Searching for Bagatelle:")

results = manager.search_routes("Bagatelle")

for route in results:
    print(route)

print("\nSearching using lowercase:")

results = manager.search_routes("bagatelle")

for route in results:
    print(route)

print("\nSearching for a destination that does not exist:")

results = manager.search_routes("Grand Baie")

if not results:
    print("No matching routes found.")