import pytest
from datetime import datetime
import areas
from project import evaluate_area, get_input_date, get_area_lat, areas_list

#TODO: It would be good to have all this tests separated into different test_files and gathered in a test folder.

areas_list = areas.create_areas_list()

def test_evaluate_area_is_valid():
    assert evaluate_area("Västernorrlands län") == "Västernorrlands län"
    assert evaluate_area("Örebro län") == "Örebro län"

def test_evaluate_area_is_invalid():
    with pytest.raises(ValueError):
        evaluate_area("asdf")

def test_get_input_date_is_valid(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "2024-09-15")
    assert get_input_date("Enter date: ") == datetime(2024, 9, 15).date()

def test_get_input_date_is_invalid(monkeypatch):
    inputs = iter(["15-09-2024", "2024-09-15"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_input_date("Enter date: ") == datetime(2024, 9, 15).date()

def test_get_input_date_is_date_in_the_future(monkeypatch):
    inputs = iter(["3000-01-01", "2024-09-15"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert get_input_date("Enter date: ") == datetime(2024, 9, 15).date()

def test_get_area_lat_is_valid():
    assert get_area_lat("Kalmar län") == (57.49484, 15.8416513)
    assert get_area_lat("Södermanlands län") == (59.3815818, 16.531456)

def test_get_area_lat_is_invalid():
    assert get_area_lat("Paris") is None
    assert get_area_lat("Berlin") is None

def test_get_area_lat_edge_cases():
    assert get_area_lat("") is None
    assert get_area_lat(None) is None
