import pytest
from src.widget import mask_account_card, get_date

@pytest.mark.parametrize(
    "account_or_card, expected",
    [
        ("Maestro 1596837868705199","Maestro 1596 83** **** 5199"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("70007922896063616361", "Введен неверный номер карты"),
        ("7OOO79228960636", "Введен неверный номер карты"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Счет 353830334744478997225", "Введен неверный номер счета"),
        ("Счет 330521648225421", "Введен неверный номер счета"),
    ],)
def test_mask_account_card(account_or_card, expected):
    assert mask_account_card(account_or_card) == expected


class TestGetDate:
    def test_valid_date(self):
        assert get_date("2023-10-15T14:30:00") == "15.10.2023"
        assert get_date("2020-01-01T00:00:00") == "01.01.2020"
        assert get_date("1999-12-31T23:59:59") == "31.12.1999"
