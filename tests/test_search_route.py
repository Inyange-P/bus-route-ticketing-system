from route_manager import RouteManager

def make_manager_with_routes():
    manager = RouteManager()
    manager.add_route("Pamplemousses", "Port Louis", 17, 40)
    manager.add_route("Port Louis", "Bagatelle", 10, 30)
    manager.add_route("Bagatelle", "Quatre Bornes", 6.2, 15)
    return manager

def test_search_matches_destination_only():
    manager = make_manager_with_routes()

    assert manager.search_routes("Bagatelle") == [manager.routes[2]]

def test_search_ignores_letter_case():
    manager = make_manager_with_routes()

    assert manager.search_routes("bagatelle") == [manager.routes[2]]

def test_search_missing_destination_returns_empty_list():
    manager = make_manager_with_routes()

    assert manager.search_routes("Grand Baie") == []
