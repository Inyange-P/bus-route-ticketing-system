from route_manager import RouteManager
from utils.file_handler import save_routes, load_routes

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
print("Saving routes:")
save_routes(manager)

new_manager = RouteManager()

print("\nLoading routes:")
load_routes(new_manager)

print("\nLoaded routes:")
new_manager.display_routes()

print("\nNext route ID:")
print(new_manager.generate_route_id())


print("\nTesting missing file:")
empty_manager = RouteManager()

load_routes(
    empty_manager,
    "file_that_does_not_exist.json"
)