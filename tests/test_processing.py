import pytest
from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(filter_state_ex):
    assert filter_by_state(filter_state_ex, state="EXECUTED") == filter_state_ex

def test_filter_by_state_cans(filter_state_cans):
    assert filter_by_state(filter_state_cans, state="CANCELED") == filter_state_cans

@pytest.mark.parametrize("input_data, expected_output", [
    ([{'date': '2023-10-01'}, {'date': '2023-09-01'}], [{'date': '2023-10-01'}, {'date': '2023-09-01'}]),
    ([{'date': '2023-09-01'}, {'date': '2023-10-01'}], [{'date': '2023-10-01'}, {'date': '2023-09-01'}]),
    ([{'date': '2023-09-01'}, {'date': '2023-09-01'}], [{'date': '2023-09-01'}, {'date': '2023-09-01'}])
])
def test_sort_by_date(input_data, expected_output):
    assert sort_by_date(input_data) == expected_output
