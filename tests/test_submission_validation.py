from datetime import date, timedelta
import pytest
import main
from utils.validation import validate_route_text


@pytest.fixture
def app(monkeypatch):
    for name, factory in [('route_manager', main.RouteManager), ('trip_manager', main.TripManager), ('passenger_manager', main.PassengerManager), ('bus_pass_manager', main.BusPassManager), ('ticket_manager', main.TicketManager)]:
        monkeypatch.setattr(main, name, factory())
    main.route_manager.add_route('Port Louis', 'Quatre Bornes', 20, 40)
    main.trip_manager.add_trip(1, date.today() + timedelta(days=30), '08:00', '09:00', 4)
    main.passenger_manager.register_passenger('Test Passenger', '57712345')
    return main


def run_menu(monkeypatch, handler, values):
    answers = iter(values)
    monkeypatch.setattr('builtins.input', lambda prompt='': next(answers))
    handler()


@pytest.mark.parametrize('value', ['', '   ', 123, None, '123', '---'])
@pytest.mark.parametrize('field', ['origin', 'destination'])
def test_route_text_rejected(app, value, field):
    assert not validate_route_text(value, field)
    values = dict(origin='Port Louis', destination='Quatre Bornes', distance_km=20, base_fare=40)
    values[field] = value
    assert app.route_manager.add_route(**values) is None
    if value is not None:  # None means keep the current value on update.
        before = vars(app.route_manager.routes[1]).copy()
        assert app.route_manager.update_route(1, **{field: value}) is None
        assert vars(app.route_manager.routes[1]) == before


@pytest.mark.parametrize('value', ['Route 66', '5th Avenue', 'District 9', 'Port Louis', 'Quatre Bornes'])
@pytest.mark.parametrize('field', ['origin', 'destination'])
def test_route_place_names_accepted(app, value, field):
    values = dict(origin='Port Louis', destination='Quatre Bornes', distance_km=20, base_fare=40)
    values[field] = value
    assert app.route_manager.add_route(**values) is not None
    assert app.route_manager.update_route(1, **{field: value}) is not None


@pytest.mark.parametrize('menu,values', [
    ('route_menu', ['4', 'abc', '0']), ('route_menu', ['5', 'abc', '0']),
    ('route_menu', ['1', 'Port Louis', 'Bagatelle', 'abc', '0']),
    ('route_menu', ['1', 'Port Louis', 'Bagatelle', '10', 'abc', '0']),
    ('trip_menu', ['1', 'abc', '0']), ('trip_menu', ['3', 'abc', '', '0']),
    ('trip_menu', ['3', '', 'bad-date', '0']), ('trip_menu', ['4', 'hello', '0']),
    ('trip_menu', ['5', 'hello', '0']), ('trip_menu', ['6', 'hello', '0']),
    ('passenger_menu', ['3', 'abc', '', '', '0']), ('passenger_menu', ['4', 'abc', '0']),
    ('passenger_menu', ['5', 'abc', '0']), ('passenger_menu', ['7', 'abc', '0']),
    ('passenger_menu', ['8', 'abc', '0']), ('ticket_menu', ['1', 'abc', '0']),
    ('ticket_menu', ['1', '1', 'hello', '0']), ('ticket_menu', ['1', '1', '1', 'abc', '0']),
    ('ticket_menu', ['1', '1', '1', '1', 'abc', '0']),
    ('ticket_menu', ['3', 'abc', '0']), ('ticket_menu', ['4', 'abc', '0']),
])
def test_bad_numeric_or_date_input_returns_to_menu(app, monkeypatch, capsys, menu, values):
    run_menu(monkeypatch, getattr(app, menu), values)
    output = capsys.readouterr().out
    assert 'Invalid' in output or 'has to be a number' in output
    assert output.count('MENU -----') >= 2


@pytest.mark.parametrize('seat', [0, -1, 5, 1])
def test_rejected_seat_returns_to_ticket_menu(app, monkeypatch, capsys, seat):
    app.ticket_manager.purchase_ticket(1, 1, 1, app.route_manager.routes, app.passenger_manager.passengers, app.trip_manager.trips)
    run_menu(monkeypatch, app.ticket_menu, ['1', '1', '1', str(seat), '', '0'])
    output = capsys.readouterr().out
    assert ('already occupied' if seat == 1 else 'does not exist') in output
    assert output.count('TICKET MENU') == 2
    assert len(app.ticket_manager.tickets) == 1


def test_route_menu_blocks_deletion_with_trip(app, monkeypatch, capsys):
    run_menu(monkeypatch, app.route_menu, ['5', '1', '0'])
    assert 'existing trips' in capsys.readouterr().out
    assert 1 in app.route_manager.routes


@pytest.mark.parametrize('departure,arrival', [('bad', ''), ('', '07:00')])
def test_trip_update_rejects_invalid_times(app, monkeypatch, capsys, departure, arrival):
    run_menu(monkeypatch, app.trip_menu, ['5', '1', '', departure, arrival, '0'])
    assert 'Invalid' in capsys.readouterr().out
    assert app.trip_manager.trips[1].departure_time == '08:00'
    assert app.trip_manager.trips[1].arrival_time == '09:00'
