from typing import Any, Callable


def log(filename: Any =None) -> Callable[[Callable[..., Any]], Any]:
    """Декоратор для логирования функций и вывода результатов в консоль или файл"""

    def wrapper(fnc: Callable) -> Any:
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                result = fnc(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{fnc.__name__} ok\n")
                else:
                    print(f"{fnc.__name__} ok\n")
                return result

            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{fnc.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{fnc.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                raise Exception("Деление на ноль невозможно")

        return inner

    return wrapper
