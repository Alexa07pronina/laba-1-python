from src.calculator import calculator_rpn
from src.constants import ROUNDING_DIGITS
def main() -> None:
    """
    Точка входа в приложение
    """

    enter_str = input("Введите выражение в обратной польской нотации или q для завершения: ")
    while enter_str!='q':
        result = calculator_rpn(enter_str)
        print("Результат:", round(result,ROUNDING_DIGITS))    #округляем результат до 2 знаков после запятой
        enter_str = input("Введите выражение в обратной польской нотации: ")

if __name__ == "__main__":
    main()
