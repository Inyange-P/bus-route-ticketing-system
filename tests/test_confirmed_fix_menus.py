import json
import os
from pathlib import Path
import subprocess
import sys

import pytest


@pytest.fixture
def saved_app(tmp_path):
    data = {
        'routes': [{'route_id': 1, 'origin': 'Port Louis', 'destination': 'Quatre Bornes', 'distance_km': 20, 'base_fare': 40}],
        'trips': [],
        'passengers': [{'passenger_id': 1, 'name': 'Alice Demo', 'phone': '57712345'}],
        'bus_passes': [{'pass_id': 1, 'passenger_id': 1, 'pass_type': 'student', 'issue_date': '2026-01-01', 'expiry_date': '2026-12-31', 'status': 'active'}],
        'tickets': [],
    }
    for name, records in data.items():
        (tmp_path / (name + '.json')).write_text(json.dumps(records))
    return tmp_path, data


def run_app(folder, answers):
    script = Path(__file__).resolve().parents[1] / 'main.py'
    result = subprocess.run(
        [sys.executable, str(script)], cwd=folder,
        input='\n'.join(answers) + '\n', text=True, capture_output=True,
        timeout=20, env={**os.environ, 'PYTHONDONTWRITEBYTECODE': '1'},
    )
    assert result.returncode == 0, result.stderr
    assert 'Exiting system.' in result.stdout
    return result.stdout


def read_saved(folder, names):
    return {name: json.loads((folder / (name + '.json')).read_text()) for name in names}


@pytest.mark.parametrize('answers,message', [
    (['3', '1', '12345', '57712345', '0', '0'], 'Invalid name'),
    (['3', '4', '1', 'Changed Name', 'WEW', '0', '0'], 'Invalid phone'),
    (['1', '1', 'Port Louis', 'Quatre Bornes', 'nan', '40', '0', '0'], 'distance must be finite'),
    (['1', '1', 'Port Louis', 'Quatre Bornes', 'inf', '40', '0', '0'], 'distance must be finite'),
    (['1', '1', 'Port Louis', 'Quatre Bornes', '20', 'nan', '0', '0'], 'fare must be finite'),
    (['1', '1', 'Port Louis', 'Quatre Bornes', '20', 'inf', '0', '0'], 'fare must be finite'),
])
def test_rejected_menu_input_preserves_saved_records(saved_app, answers, message):
    folder, before = saved_app
    assert message in run_app(folder, answers)
    assert read_saved(folder, before) == before


def test_suspend_issue_renew_menu_preserves_old_pass(saved_app):
    folder, original = saved_app
    output = run_app(folder, ['3', '8', '1', '5', '1', 'student',
                              '2026-01-01', '2026-12-31', '0', '0'])
    assert 'Pass suspended successfully.' in output
    assert 'Bus pass issued successfully.' in output
    before = read_saved(folder, original)
    output = run_app(folder, ['3', '7', '1', '2027-12-31', '0', '0'])
    assert 'another active pass' in output
    after = read_saved(folder, original)
    assert after == before
    assert after['bus_passes'][0]['status'] == 'suspended'
    assert sum(p['status'] == 'active' for p in after['bus_passes']) == 1
