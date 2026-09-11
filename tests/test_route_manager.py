from route_manager import RouteManager
from route import Route

manager = RouteManager()    

print("Next route ID:", manager.generate_route_id())

route = Route(
    route_id=1,
    origin="Pamplemousses",
    destination="Port Louis",
    distance_km=17,
    base_fare=40
)

manager.routes[route.route_id] = route

print("Next route ID:", manager.generate_route_id())