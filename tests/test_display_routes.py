from route_manager import RouteManager


def test_display_empty_routes(capsys):
    # capsys captures printed output so pytest can check it.
    manager = RouteManager()
    manager.display_routes()

    assert capsys.readouterr().out.strip() == "No routes available."


def test_display_routes_shows_each_route(capsys):
    manager = RouteManager()
    route1 = manager.add_route("Pamplemousses", "Port Louis", 17, 40)
    route2 = manager.add_route("Port Louis", "Bagatelle", 10, 30)

    manager.display_routes()
    output = capsys.readouterr().out

    assert "AVAILABLE ROUTES" in output
    assert str(route1) in output
    assert str(route2) in output
