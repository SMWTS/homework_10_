import logging

masks_logger = logging.getLogger("masks_log")
masks_logger.setLevel(logging.DEBUG)
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler = logging.FileHandler("../logs/masks.log", encoding="utf-8")
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция принимает на вход номер карты и маскирует его"""
    masks_logger.info(f"Получение номера карты: {card_number}")
    if card_number == " ":
        masks_logger.info("Проверяем что строка не пустая")
        masks_logger.error("Произошла ошибка. Строка пуста")
        return "Пустая строка. Введите номер карты"
    card_number_split = card_number.split()
    card_name = card_number_split[:-1]
    card_name_join = " ".join(card_name)
    card_num = card_number_split[-1]

    # Проверяем хватает цифр в номере карты
    if len(card_num) != 16:
        masks_logger.info("Проверяем хватает цифр в номере карты")
        masks_logger.error("Произошла ошибка. Введен неверный номер карты")
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
    masks_logger.info(f"Вывод замаскированного номер карты {masked_card_result_with_space}")
    return f"{card_name_join} {masked_card_result_with_space}"


if __name__ == "__main__":
    print(get_mask_card_number("Visa Platinum 8990922113665229"))


def get_mask_account(card_account: str) -> str:
    """Функция принимает номер счета и маскирует его,
    видны только последние 4 цифры номера, а перед ними **"""
    masks_logger.info(f"Получение номера счета: {card_account}")
    if card_account == " ":
        masks_logger.info("Проверяем что строка не пустая")
        masks_logger.error("Произошла ошибка. Строка пуста")
        return "Пустая строка. Введите номер счета"
    card_account_split = card_account.split()
    account_name = card_account_split[0]
    account_num = card_account_split[-1]
    if len(account_num) != 20 or account_name != "Счет":
        masks_logger.info("Проверяем хватает цифр в номере счета")
        masks_logger.error("Произошла ошибка. Введен неверный номер счета")
        return "Введен неверный номер счета"

    last_part = str(account_num[-4:])
    masks_logger.info(f"Вывод замаскированного номера счета {account_name} **{last_part}")
    return f"{account_name} **{last_part}"


if __name__ == "__main__":
    print(get_mask_account("Счет 33052164820025421951"))
