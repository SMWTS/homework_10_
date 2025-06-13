import json
import logging
import os

utils_logger = logging.getLogger("utils_log")
utils_logger.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("../logs/utils.log", encoding="utf-8")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)


def get_transactions(json_path: str) -> list:
    """
    Считывает JSON-файл и возвращает список словарей с транзакциями.
    Если файл отсутствует, пуст, или не содержит список — возвращает пустой список.
    """
    if not os.path.exists(json_path):
        utils_logger.info("Начало работы функции 'get_transactions'")
        return []
    try:
        with open(json_path, encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return []
            if isinstance(data, list):
                return data
            else:
                return []
    except (OSError, IOError):
        utils_logger.error("Произошла ошибка.")
        return []


if __name__ == "__main__":
    print()
