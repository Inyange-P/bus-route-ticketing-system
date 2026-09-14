from route_manager import RouteManager

def test_update_fare_keeps_other_details():
    manager = RouteManager()
    route = manager.add_route("Pamplemousses", "Port Louis", 17, 40)

    updated_route = manager.update_route(1, base_fare=45)

    assert updated_route is route
    assert manager.routes[1] is route
    assert route.base_fare == 45
    assert route.origin == "Pamplemousses"
    assert route.destination == "Port Louis"
    assert route.distance_km == 17

def test_update_destination_and_distance():
    manager = RouteManager()
    route = manager.add_route("Pamplemousses", "Port Louis", 17, 40)

    updated_route = manager.update_route(1, destination="Grand Baie", distance_km=20)

    assert updated_route is route
    assert route.destination == "Grand Baie"
    assert route.distance_km == 20
    assert route.origin == "Pamplemousses"
    assert route.base_fare == 40

def test_update_missing_route_returns_none():
    manager = RouteManager()
    route = manager.add_route("Pamplemousses", "Port Louis", 17, 40)

    assert manager.update_route(99, base_fare=100) is None
    assert manager.routes == {1: route}
    assert route.base_fare == 40
