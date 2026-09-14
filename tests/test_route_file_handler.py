from route_manager import RouteManager
from utils.file_handler import save_routes, load_routes

def test_save_and_load_routes_preserves_details_and_next_id(tmp_path):
    # tmp_path gives this test its own folder, leaving saved project data alone.
    filename = tmp_path / "routes.json"
    manager = RouteManager()
    manager.add_route("Pamplemousses", "Port Louis", 17, 40)
    manager.add_route("Port Louis", "Bagatelle", 10, 30)

    save_routes(manager, filename)
    new_manager = RouteManager()
    load_routes(new_manager, filename)

    assert set(new_manager.routes) == {1, 2}
    for route_id, original in manager.routes.items():
        loaded = new_manager.routes[route_id]
        assert loaded.route_id == original.route_id
        assert loaded.origin == original.origin
        assert loaded.destination == original.destination
        assert loaded.distance_km == original.distance_km
        assert loaded.base_fare == original.base_fare
    assert new_manager.generate_route_id() == 3

def test_load_missing_file_leaves_manager_empty(tmp_path):
    manager = RouteManager()

    load_routes(manager, tmp_path / "file_that_does_not_exist.json")

    assert manager.routes == {}
    assert manager.generate_route_id() == 1
