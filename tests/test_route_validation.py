from route_manager import RouteManager

def test_add_valid_route():
    manager = RouteManager()

    route = manager.add_route("Pamplemousses", "Port Louis", 17, 40)

    assert route is not None
    assert manager.routes == {1: route}

def test_add_route_rejects_empty_origin():
    manager = RouteManager()

    assert manager.add_route("", "Bagatelle", 12, 30) is None
    assert manager.routes == {}
    assert manager.generate_route_id() == 1

def test_add_route_rejects_empty_destination():
    manager = RouteManager()

    assert manager.add_route("Port Louis", "", 12, 30) is None
    assert manager.routes == {}
    assert manager.generate_route_id() == 1

def test_add_route_rejects_negative_distance():
    manager = RouteManager()

    assert manager.add_route("Port Louis", "Bagatelle", -5, 30) is None
    assert manager.routes == {}
    assert manager.generate_route_id() == 1

def test_add_route_rejects_negative_fare():
    manager = RouteManager()

    assert manager.add_route("Port Louis", "Bagatelle", 12, -10) is None
    assert manager.routes == {}
    assert manager.generate_route_id() == 1

def test_invalid_update_leaves_original_route_unchanged():
    manager = RouteManager()
    route = manager.add_route("Pamplemousses", "Port Louis", 17, 40)

    assert manager.update_route(1, destination="") is None
    assert manager.routes == {1: route}
    assert route.origin == "Pamplemousses"
    assert route.destination == "Port Louis"
    assert route.distance_km == 17
    assert route.base_fare == 40
