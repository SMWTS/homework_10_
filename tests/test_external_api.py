from typing import Any
from unittest import result
from unittest.mock import Mock, patch

from src.external_api import get_currency_usd_or_euro, get_the_transaction_amount
from src.utils import get_transactions


@patch("requests.request")
def test_get_the_transaction_amount(mock_request) -> Any:
    mock_response = mock_request.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 100.0}

    transaction = {"operationAmount": {"amount": "10", "currency": {"code": "USD"}}}
    resultate = get_the_transaction_amount(transaction)
    assert resultate == 100.0


@patch("json.load")
@patch("builtins.open")
def test_get_transactions(mock_load=Any, transact=None) -> Any:
    operation_amount = transact.get("operationAmount")
    if operation_amount is not None:
        amount = float(operation_amount.get("amount"))
        return amount
    else:
        mock_load.return_value = [{"test": "test"}]
        assert get_transactions(mock_load) == [{"test": "test"}]
        return mock_load.assert_called()


@patch("requests.request")
def test_get_the_transaction_amount_error(mock_request=None) -> Any:
    """Тест если есть нет сети и валюта RUB"""
    mock_response = mock_request.return_value
    mock_response.status_code = 500
    mock_response.json.return_value = "Проблема с сервером"

    transaction = {"operationAmount": {"amount": "Проблема с сервером", "currency": {"code": "RUB"}}}
    result_1 = get_the_transaction_amount(transaction)
    assert result_1 == "Проблема с сервером"


from unittest.mock import patch


@patch("requests.request")
def test_get_currency_usd_or_euro(mock_request):
    mock_response = mock_request.return_value
    mock_response.status_code = 200
    mock_response.json.return_value = {"result": 100.0}

    transaction = {"operationAmount": {"amount": "10", "currency": {"code": "USD"}}}
    result_2 = get_currency_usd_or_euro(transaction)
    assert result_2 == 100.0
