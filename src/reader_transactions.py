import csv
from typing import Any, Hashable

import pandas as pd


def get_read_csv(path: str) -> list[dict]:
    """Функция принимает файл CSV и возвращает список словарей"""
    csv_list = []
    with open(path, encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=";")
        for row in reader:
            my_dict = {
                "id": row["id"],
                "state": row["state"],
                "date": row["date"],
                "amount": row["amount"],
                "currency_name": row["currency_name"],
                "currency_code": row["currency_code"],
                "from": row["from"],
                "to": row["to"],
                "description": row["description"],
            }
            csv_list.append(my_dict)
    return csv_list


def get_read_xlsx(path: str) -> list[dict[Hashable, Any]]:
    """Функция принимает файл Excel и возвращает список словарей"""
    with open(path, encoding="utf-8") as my_dict:
        excel_data = pd.read_excel(path)
        my_dict = excel_data.to_dict(orient="records")
    return my_dict
