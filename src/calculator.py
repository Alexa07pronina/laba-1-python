from src.function import correct_enter,correct_bracket,division,pow,percent,int_division
from src.constants import OPS

def calculator_rpn(enter_str:str ) -> float:
    """
    Реализация калькулятора rpn
    """
    correct_enter(enter_str.replace(')',' ) ').replace('(', ' ( ').split()) #проверяем корректный ввод
    enter_str = correct_bracket(enter_str)    #проверяем выражения в скобках
    lst = enter_str.split()

    st: list[float] = []
    for tok in lst:
        if tok in OPS:
            if tok =='~':     #унарный минус
                a = st.pop()
                st.append(-a)
                continue
            if tok=='|':      #модуль
                a=st.pop()
                st.append(abs(a))
                continue
            if len(st) < 2:
                print(ValueError("\033[31m{}".format("Дефицит или избыток операндов")))
                exit(0)
            b = st.pop()  # второе число
            a = st.pop()  # первое число
            if tok == "+":
                st.append(a + b)
            elif tok == "-":
                st.append(a - b)
            elif tok == "*":
                st.append(a * b)
            elif tok == "/":
                st.append(division(a,b))
            elif tok =='**':
                st.append(pow(a,b))
            elif tok =='//':
                st.append(int_division(a,b))
            elif tok== '%':
                st.append(percent(a,b))
        else:
            try:
                st.append(float(tok))
            except ValueError:
                print("\033[31m{}".format("Недопустимые символы в выражении"))
                exit(0)
    if len(st)!=1:
        print(ValueError("\033[31m{}".format("Дефицит или избыток операндов")))
        exit(0)

    return st[0]
