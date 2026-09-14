from route_manager import RouteManager
from route import Route

def test_new_manager_starts_empty_with_first_id():
    manager = RouteManager()

    assert manager.routes == {}
    assert manager.generate_route_id() == 1

def test_next_route_id_follows_highest_stored_id():
    manager = RouteManager()
    route = Route(1, "Pamplemousses", "Port Louis", 17, 40)
    manager.routes[route.route_id] = route

    assert manager.generate_route_id() == 2

    manager.routes[5] = Route(5, "Port Louis", "Bagatelle", 12, 30)
    assert manager.generate_route_id() == 6
