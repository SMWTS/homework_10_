import re
from collections import Counter


def filter_operations_by_description(data: list[dict], search: str) -> list[dict]:
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [operation for operation in data if pattern.search(operation.get("description", ""))]


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Подсчитывает количество операций по категориям, используя Counter.
    """
    category_counter = Counter()

    for operation in data:
        desc = operation.get("description", "").lower()
        for category in categories:
            if category.lower() in desc:
                category_counter[category] += 1
                break

    return dict(category_counter)
