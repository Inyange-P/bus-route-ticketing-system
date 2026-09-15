from passenger_manager import PassengerManager
from bus_pass_manager import BusPassManager
from ticket import Ticket
from utils.file_handler import (
    save_tickets, load_tickets, save_passengers, load_passengers,
    save_bus_passes, load_bus_passes,
)


def test_passengers_round_trip(tmp_path):
    manager = PassengerManager()
    manager.register_passenger('Alice Demo', '57712345')
    manager.register_passenger('Ben Demo', '58812345')
    filename = tmp_path / 'passengers.json'
    save_passengers(manager.passengers, filename)
    loaded = load_passengers(filename)
    assert set(loaded) == set(manager.passengers)
    for passenger_id, passenger in manager.passengers.items():
        assert vars(loaded[passenger_id]) == vars(passenger)


def test_bus_passes_round_trip(tmp_path):
    manager = BusPassManager()
    passengers = PassengerManager()
    passengers.register_passenger('Alice Demo', '57712345')
    bus_pass = manager.issue_pass(1, 'student', '2026-01-01', '2027-01-01',
                                  passengers=passengers.passengers)
    filename = tmp_path / 'bus_passes.json'
    save_bus_passes(manager.bus_passes, filename)
    loaded = load_bus_passes(filename)
    assert set(loaded) == {1}
    assert vars(loaded[1]) == vars(bus_pass)


def test_tickets_round_trip(tmp_path):
    ticket = Ticket(ticket_id=1, passenger_id=1, trip_id=1, seat_number=5, price=50)
    filename = tmp_path / 'tickets.json'
    save_tickets({1: ticket}, filename)
    loaded = load_tickets(filename)
    assert set(loaded) == {1}
    assert vars(loaded[1]) == vars(ticket)
