from datetime import date, datetime
import pytest
import main
from bus_pass_manager import BusPassManager
from passenger_manager import PassengerManager
from route_manager import RouteManager
from trip_manager import TripManager
from ticket_manager import TicketManager


@pytest.fixture
def records():
    passengers = PassengerManager()
    passengers.register_passenger('Alice Demo', '57712345')
    passengers.register_passenger('Ben Demo', '58812345')
    passes = BusPassManager()
    return passengers, passes


def test_issue_pass_requires_existing_passenger(records, capsys):
    passengers, passes = records
    assert passes.issue_pass(99, 'student', '2026-12-10', '2026-12-20', passengers.passengers) is None
    assert 'does not exist' in capsys.readouterr().out
    assert passes.bus_passes == {}
    assert passes.generate_pass_id() == 1


def test_issue_pass_requires_passenger_records(records, capsys):
    _, passes = records
    assert passes.issue_pass(1, 'student', '2026-12-10', '2026-12-20') is None
    assert 'passenger records are required' in capsys.readouterr().out
    assert passes.bus_passes == {}


def test_existing_passenger_cannot_hold_two_active_passes(records, capsys):
    passengers, passes = records
    first = passes.issue_pass(1, 'student', '2026-12-10', '2026-12-20', passengers.passengers)
    assert first is not None
    assert passes.issue_pass(1, 'senior', '2026-12-10', '2026-12-20', passengers.passengers) is None
    assert 'already has an active pass' in capsys.readouterr().out
    assert passes.bus_passes == {1: first}


@pytest.mark.parametrize('travel_date,passenger_id,status,expected_price', [
    (date(2026, 12, 9), 1, 'active', 40),
    (date(2026, 12, 10), 1, 'active', 20),
    (date(2026, 12, 20), 1, 'active', 20),
    (date(2026, 12, 21), 1, 'active', 40),
    (date(2026, 12, 15), 2, 'active', 40),
    (date(2026, 12, 15), 1, 'suspended', 40),
    (date(2026, 12, 15), 1, 'cancelled', 40),
])
@pytest.mark.parametrize('date_type', [str, date, datetime])
def test_pass_boundaries_status_and_ownership(records, travel_date, passenger_id, status, expected_price, date_type):
    passengers, passes = records
    issue, expiry = '2026-12-10', '2026-12-20'
    if date_type is date:
        issue, expiry = date.fromisoformat(issue), date.fromisoformat(expiry)
    elif date_type is datetime:
        issue, expiry = datetime.fromisoformat(issue), datetime.fromisoformat(expiry)
    bus_pass = passes.issue_pass(1, 'student', issue, expiry, passengers.passengers)
    bus_pass.status = status
    assert passes.is_pass_valid(1, travel_date, passenger_id) is (expected_price == 20)
    routes = RouteManager()
    routes.add_route('Port Louis', 'Quatre Bornes', 20, 40)
    trips = TripManager()
    trips.add_trip(1, travel_date, '08:00', '09:00', 4)
    tickets = TicketManager()
    ticket = tickets.purchase_ticket(passenger_id, 1, 1, routes.routes, passengers.passengers, trips.trips, passes.bus_passes, 1)
    assert ticket.price == expected_price
    assert ticket.pass_id == (1 if expected_price == 20 else None)
    assert tickets.tickets == {1: ticket}


def test_menu_supplies_current_passenger_records(records, monkeypatch, capsys):
    passengers, passes = records
    monkeypatch.setattr(main, 'passenger_manager', passengers)
    monkeypatch.setattr(main, 'bus_pass_manager', passes)
    answers = iter(['5', '99', 'student', '2026-12-10', '2026-12-20',
                    '5', '1', 'student', '2026-12-10', '2026-12-20', '0'])
    monkeypatch.setattr('builtins.input', lambda prompt='': next(answers))
    main.passenger_menu()
    output = capsys.readouterr().out
    assert 'does not exist' in output
    assert 'Bus pass issued successfully.' in output
    assert len(passes.bus_passes) == 1
    assert passes.bus_passes[1].passenger_id == 1
