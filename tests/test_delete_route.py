import pytest

from route_manager import RouteManager


class DummyTrip:
    def __init__(self, trip_id, route_id):
        self.trip_id = trip_id
        self.route_id = route_id


def test_delete_route_removes_only_selected_route():
    manager = RouteManager()
    manager.add_route("Pamplemousses", "Port Louis", 17, 40)
    remaining_route = manager.add_route("Port Louis", "Mahebourg", 47, 65)

    assert manager.delete_route(1) is True
    assert manager.routes == {2: remaining_route}


def test_delete_missing_route_returns_false():
    manager = RouteManager()
    route = manager.add_route("Pamplemousses", "Port Louis", 17, 40)

    assert manager.delete_route(99) is False
    assert manager.routes == {1: route}


def test_delete_route_with_existing_trip_is_blocked():
    manager = RouteManager()
    route = manager.add_route("Port Louis", "Mahebourg", 47, 65)
    trips = {1: DummyTrip(1, route.route_id)}

    with pytest.raises(ValueError, match="existing trips"):
        manager.delete_route(route.route_id, trips)

    assert manager.routes == {route.route_id: route}
