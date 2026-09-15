from route import Route

def test_route_stores_details():
    route = Route(1, "Pamplemousses", "Port Louis", 17, 40)

    assert route.route_id == 1
    assert route.origin == "Pamplemousses"
    assert route.destination == "Port Louis"
    assert route.distance_km == 17
    assert route.base_fare == 40

def test_route_string_shows_details():
    route = Route(1, "Pamplemousses", "Port Louis", 17, 40)

    assert str(route) == (
        "Route ID: 1 | Origin: Pamplemousses | Destination: Port Louis | "
        "Distance: 17 km | Base Fare: Rs 40.00"
    )
