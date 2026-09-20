import pytest
from passenger_manager import PassengerManager
from utils.validation import validate_name


@pytest.mark.parametrize('name,valid', [
    ('John Smith', True), ('', False), ('   ', False), ('12345', False),
    ('John123', True), (12345, False), (None, False), ([], False),
])
def test_passenger_name_content(name, valid):
    assert validate_name(name) is valid
    manager = PassengerManager()
    passenger = manager.register_passenger(name, '57712345')
    assert (passenger is not None) is valid
    assert len(manager.passengers) == int(valid)


@pytest.mark.parametrize('name,phone,valid', [
    ('Jane Smith', '58812345', True),
    ('Jane Smith', 'WEW', False),
    ('12345', '58812345', False),
])
def test_passenger_update_is_atomic(name, phone, valid):
    manager = PassengerManager()
    passenger = manager.register_passenger('John Smith', '57712345')
    before = vars(passenger).copy()
    updated = manager.update_passenger(1, name=name, phone=phone)
    if valid:
        assert updated is passenger
        assert passenger.name == name
        assert passenger.phone == phone
    else:
        assert updated is None
        assert vars(passenger) == before


@pytest.mark.parametrize('field', ['distance_km', 'base_fare'])
@pytest.mark.parametrize('value', [float('nan'), float('inf'), float('-inf')])
def test_nonfinite_route_numbers_rejected(field, value):
    from route_manager import RouteManager
    manager = RouteManager()
    route = manager.add_route('Port Louis', 'Quatre Bornes', 20, 40)
    before = vars(route).copy()
    values = dict(origin='Port Louis', destination='Quatre Bornes', distance_km=20, base_fare=40)
    values[field] = value
    assert manager.add_route(**values) is None
    assert manager.update_route(1, **{field: value}) is None
    assert vars(route) == before
    assert manager.routes == {1: route}


@pytest.mark.parametrize('distance,fare', [(20, 40), (0.5, 0), (12.5, 15.75)])
def test_finite_route_numbers_accepted(distance, fare):
    from utils.validation import validate_distance, validate_fare
    assert validate_distance(distance)
    assert validate_fare(fare)


@pytest.mark.parametrize('status', ['active', 'suspended'])
def test_normal_pass_renewal(status):
    from bus_pass_manager import BusPassManager
    passengers = PassengerManager()
    passengers.register_passenger('John Smith', '57712345')
    manager = BusPassManager()
    bus_pass = manager.issue_pass(1, 'student', '2026-01-01', '2026-12-31', passengers.passengers)
    manager.set_pass_status(1, status)
    assert manager.renew_pass(1, '2027-12-31') is bus_pass
    assert bus_pass.expiry_date == '2027-12-31'
    assert bus_pass.status == 'active'


def test_renewal_rejects_competing_active_pass(capsys):
    from bus_pass_manager import BusPassManager
    passengers = PassengerManager()
    passengers.register_passenger('John Smith', '57712345')
    manager = BusPassManager()
    old_pass = manager.issue_pass(1, 'student', '2026-01-01', '2026-12-31', passengers.passengers)
    manager.set_pass_status(1, 'suspended')
    new_pass = manager.issue_pass(1, 'senior', '2026-01-01', '2026-12-31', passengers.passengers)
    before = {key: vars(value).copy() for key, value in manager.bus_passes.items()}
    assert manager.renew_pass(old_pass.pass_id, '2027-12-31') is None
    assert 'another active pass' in capsys.readouterr().out
    assert {key: vars(value) for key, value in manager.bus_passes.items()} == before
    assert [p for p in manager.bus_passes.values() if p.status == 'active'] == [new_pass]
