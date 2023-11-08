import pytest
from fastapi.testclient import TestClient

from medgarant_fastapi_test.api import app

client = TestClient(app)

expected_2 = [
    {'start': '09:00', 'stop': '09:30'},
    {'start': '09:30', 'stop': '10:00'},
    {'start': '10:00', 'stop': '10:30'},
    {'start': '10:50', 'stop': '11:20'},
    {'start': '11:20', 'stop': '11:50'},
    {'start': '11:50', 'stop': '12:20'},
    {'start': '12:20', 'stop': '12:50'},
    {'start': '12:50', 'stop': '13:20'},
    {'start': '13:20', 'stop': '13:50'},
    {'start': '13:50', 'stop': '14:20'},
    {'start': '15:50', 'stop': '16:20'},
    {'start': '17:20', 'stop': '17:50'},
    {'start': '17:50', 'stop': '18:20'},
    {'start': '18:50', 'stop': '19:20'},
    {'start': '19:20', 'stop': '19:50'},
    {'start': '20:20', 'stop': '20:50'}
]
expected_3 = [
    {'start': '09:00', 'stop': '09:50'},
    {'start': '10:50', 'stop': '11:40'},
    {'start': '11:40', 'stop': '12:30'},
    {'start': '12:30', 'stop': '13:20'},
    {'start': '13:20', 'stop': '14:10'},
    {'start': '15:50', 'stop': '16:40'},
    {'start': '17:20', 'stop': '18:10'},
    {'start': '18:50', 'stop': '19:40'}
]

expected_4 = [
    {'start': '09:00', 'stop': '09:40'},
    {'start': '09:40', 'stop': '10:20'},
    {'start': '10:50', 'stop': '11:30'},
    {'start': '11:30', 'stop': '12:10'},
    {'start': '12:10', 'stop': '12:50'},
    {'start': '12:50', 'stop': '13:30'},
    {'start': '13:30', 'stop': '14:10'},
    {'start': '15:50', 'stop': '16:30'},
    {'start': '17:20', 'stop': '18:00'},
    {'start': '18:00', 'stop': '18:40'},
    {'start': '18:50', 'stop': '19:30'},
    {'start': '20:20', 'stop': '21:00'}
]


def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {'message': 'Hello, world!'}


@pytest.mark.parametrize('minutes, expected', [(None, expected_2),
                                               (50, expected_3),
                                               (40, expected_4)])
def test_get_times(minutes, expected):
    if minutes is None:
        response = client.get('/times')
    else:
        response = client.get(f'/times/?minutes={minutes}')
    assert response.status_code == 200
    assert response.json() == expected

