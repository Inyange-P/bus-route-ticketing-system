from route_manager import RouteManager


def test_add_routes_stores_routes_with_different_ids():
    manager = RouteManager()

    route1 = manager.add_route("Pamplemousses", "Port Louis", 17, 40)
    route2 = manager.add_route("Port Louis", "Bagatelle", 12, 30)

    assert route1.route_id == 1
    assert route2.route_id == 2
    assert manager.routes == {1: route1, 2: route2}
    assert route1.origin == "Pamplemousses"
    assert route1.destination == "Port Louis"
    assert route1.distance_km == 17
    assert route1.base_fare == 40
    assert route2.origin == "Port Louis"
    assert route2.destination == "Bagatelle"
    assert route2.distance_km == 12
    assert route2.base_fare == 30
    assert manager.generate_route_id() == 3
