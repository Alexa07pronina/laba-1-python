import re
def correct_bracket(enter_str:str) -> str:
    """
    Функция обработки правильности выражения в скобках
    """
    chars=['+', '-', '*', '/', '%', '|','@','$']   #список символов для подсчета

    enter_str=enter_str.replace('//','@').replace('**','$')
    finish=0
    start=0
    while ')' in enter_str:
        finish = enter_str.index(')')
        start = enter_str[:finish].rindex('(')
        temporary_str=enter_str[start+1:finish]
        count_numbers = len(re.findall(r'-?\d+\.?\d*', temporary_str))      #подсчет всех чисел в строке
        count_simbols = sum(temporary_str.count(char) for char in chars)     #подсчет всех операций в строке
        if count_numbers-count_simbols!=1:
            print(ValueError("\033[31m{}".format("Некорректное выражение в скобках")))
            exit(0)
        else:
            enter_str = enter_str[:start]+' '+temporary_str +' '+ enter_str[finish+1:]
    return enter_str.replace('$','**').replace('@','//')

def correct_enter(lst:list) -> None:
    """
    Обработка ошибок ввода
    """
    try:
        if not lst:
            raise ValueError
    except ValueError:
        print("\033[31m{}".format("Выражение не может быть пустым"))
        exit(0)
    try:
        if lst[0][0] not in '0123456789().':
            raise ValueError
    except ValueError:
        print("\033[31m{}".format("Выражение должно начинаться с числа или ()"))
        exit(0)
    try:
        if '(' in lst or ')' in lst:
            if lst.count('(')!=lst.count(')') or lst.index(')')< lst.index('('):
                raise ValueError
    except ValueError:
        print("\033[31m{}".format("Некорректное выражение: скобки введены неверно"))
        exit(0)
    try:
        if sum(1 for char in ''.join(lst) if char.isalpha()) != 0:
            raise ValueError
    except ValueError:
        print("\033[31m{}".format("Нельзя использовать буквы"))
        exit(0)


def division(a:float, b:float) -> float:
     """
     Функция деления
     """
     try:
         return a / b
     except ZeroDivisionError:
         print("\033[31m{}".format("Деление на 0 недопустимо!"))
         exit(0)


def int_division(a: float, b: float) -> float:
     """
     Функция целочисленного деления
     """
     if str(a)[-2:] == '.0':
          a = int(a)
     if str(b)[-2:] == '.0':
          b = int(b)
     try:
         if not (str(abs(a)).isdigit() and str(abs(b)).isdigit()):
              raise ValueError
     except ValueError:
         print("\033[31m{}".format("// применимо только к целым числам!"))
         exit(0)
     try:
         return a//b
     except ZeroDivisionError:
         print("\033[31m{}".format("Деление на 0 недопустимо!"))
         exit(0)
def percent(a: float, b: float) -> float:
     """
     Функция нахождения остатка от деления
     """
     if str(a)[-2:] == '.0':
          a = int(a)
     if str(b)[-2:] == '.0':
          b = int(b)
     try:
         if not (str(abs(a)).isdigit() and str(abs(b)).isdigit()):
             raise ValueError
     except ValueError:
         print("\033[31m{}".format("% применимо только к целым числам!"))
         exit(0)
     try:
         return a % b
     except ZeroDivisionError:
         print("\033[31m{}".format("Деление на 0 недопустимо!"))
         exit(0)

def pow(a: float, b: float) -> float:
     """
     Функция возведения в степень
     """
     try:
          return a**b
     except OverflowError:
          print("\033[31m{}".format("Слишком большие числа"))
          exit(0)
