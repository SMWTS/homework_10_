import sys
from typing import List, Dict, Any

import pandas as pd

from src.process_bank import filter_operations_by_description
from src.reader_transactions import load_csv, load_json, load_xlsx

def main() -> None:
    print("Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")

    menu_options: Dict[str, str] = {
        '1': 'Получить информацию о транзакциях из JSON-файла',
        '2': 'Получить информацию о транзакциях из CSV-файла',
        '3': 'Получить информацию о транзакциях из XLSX-файла'
    }

    for key, desc in menu_options.items():
        print(f"{key}. {desc}")

    choice: str = input()

    data: List[Dict[str, Any]] = []

    if choice == '1':
        print("Программа: Для обработки выбран JSON-файл.")
        file_path: str = input("Введите путь к JSON-файлу: ")
        print(f"Пытаюсь загрузить файл по пути: {file_path}")
        try:
            data = load_json(file_path)
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            sys.exit()

    elif choice == '2':
        print("Программа: Для обработки выбран CSV-файл.")
        file_path_csv: str = input("Введите путь к CSV-файлу: ")
        print(f"Пытаюсь загрузить файл по пути: {file_path_csv}")
        try:
            data = load_csv(file_path_csv)
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            sys.exit()

    elif choice == '3':
        print("Программа: Для обработки выбран XLSX-файл.")
        file_path_xlsx: str = input("Введите путь к XLSX-файлу: ")
        print(f"Пытаюсь загрузить файл по пути: {file_path_xlsx}")
        try:
            data = load_xlsx(file_path_xlsx)
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            sys.exit()
    else:
        print("Некорректный выбор.")
        sys.exit()

    # Ввод статуса
    valid_statuses: List[str] = ['EXECUTED', 'CANCELED', 'PENDING']
    status: str = ''
    while True:
        status = input("Введите статус, по которому необходимо выполнить фильтрацию: ").upper()
        if status in valid_statuses:
            print(f"Программа: Операции отфильтрованы по статусу \"{status}\"")
            break
        else:
            print(f"Статус операции \"{status}\" недоступен.")
            print("Пожалуйста, введите один из следующих статусов: EXECUTED, CANCELED, PENDING.")

    # Фильтрация по статусу
    filtered_data: List[Dict[str, Any]] = [op for op in data if op.get('status', '').upper() == status]

    # Сортировка по дате
    sort_choice: str = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice == 'да':
        order: str = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        reverse: bool = True if order in ['по убыванию', 'убывание'] else False
        try:
            for op in filtered_data:
                op['date_obj'] = pd.to_datetime(op.get('date', ''), errors='coerce')
            filtered_data.sort(key=lambda x: x['date_obj'], reverse=reverse)
        except Exception:
            print("Ошибка сортировки по дате.")
        # Удаляем временный ключ
        for op in filtered_data:
            if 'date_obj' in op:
                del op['date_obj']

    # Фильтрация по валюте
    currency_choice: str = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if currency_choice == 'да':
        filtered_data = [op for op in filtered_data if 'руб' in str(op.get('amount', '')).lower()]

    # Фильтр по слову в описании
    desc_filter_choice: str = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if desc_filter_choice == 'да':
        search_word: str = input("Введите слово для поиска: ")
        filtered_data = filter_operations_by_description(filtered_data, search_word)

    # Итоговая проверка
    if not filtered_data:
        print("Программа: Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
        return

    # Вывод операций
    print("Распечатываю итоговый список транзакций...\n")
    print(f"Всего банковских операций в выборке: {len(filtered_data)}\n")
    for op in filtered_data:
        date_str: str = op.get('date', '')
        description: str = op.get('description', '')
        amount: str = op.get('amount', '')
        print(f"{date_str} {description}\nСумма: {amount}\n")
