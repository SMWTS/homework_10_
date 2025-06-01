from datetime import datetime


def mask_account_card(account_or_card: str) -> str:
    """Функция принимает тип и номер карты или счета и возвращает строку с замаскированным номером"""
    account_or_card_split = account_or_card.split()

    if "Счет" in account_or_card:
        if len(account_or_card_split[-1]) != 20:
            return "Введен неверный номер счета"
        elif len(account_or_card) == " ":
            return "Пустая строка. Введите номер карты или счета"
        else:
            number_mask = "**" + account_or_card[-4:]
            return f"Счет {number_mask}"
    else:
        if len(account_or_card_split[-1]) != 16:
            return "Введен неверный номер карты"
        elif len(account_or_card) == " ":
            return "Пустая строка. Введите номер карты или счета"
        else:
            card_type_sep = " ".join(account_or_card_split[:-1])
            card_number_sep = account_or_card_split[-1]
            number_mask = "" + card_number_sep[0:4] + " " + card_number_sep[4:6] + "** **** " + card_number_sep[-4:]
            return f"{card_type_sep} {number_mask}"


def get_date(date: str) -> str:
    """Функция, которая преобразовывает формат даты в "ДД.ММ.ГГГГ" """

    date_obj = datetime.fromisoformat(date)
    formatted_date = date_obj.strftime("%d.%m.%Y")
    return formatted_date
