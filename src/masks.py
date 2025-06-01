def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и маскирует его"""
    if card_number == ' ':
        return "Пустая строка. Введите номер карты"
    card_number_split = card_number.split()
    card_name = card_number_split[:-1]
    card_num = card_number_split[-1]

    # Проверяем хватает цифр в номере карты
    if len(card_num) != 16:
        return "Введен неверный номер карты"

    result = []
    # Список для хранения замаскированного номера карты
    counter = 0
    # Счетчик цифр в номере карты, чтобы знать, какую заменить на *
    for number in card_num:
        counter += 1
        if 6 < counter <= len(card_num) - 4:
            result.append("*")
        else:
            result.append(number)
    masked_card = "".join(result)
    masked_card_result = []

    # список для хранения по четыре цифры номера карты
    for i in range(0, len(masked_card), 4):
        masked_card_result.append(masked_card[i : i + 4])
    masked_card_result_with_space = " ".join(masked_card_result)
    return masked_card_result_with_space


def get_mask_account(card_account: str) -> str:
    """Функция принимает номер счета и маскирует его,
    видны только последние 4 цифры номера, а перед ними **"""
    if card_account == ' ':
        return "Пустая строка. Введите номер счета"
    card_account_split = card_account.split()
    account_name = card_account_split[0]
    account_num = card_account_split[-1]
    if len(account_num) != 20 or account_name != "Счет":
        return "Введен неверный номер счета"

    last_part = str(account_num[-4:])
    return f"{account_name} **{last_part}"
