from src.calculator import calculator_rpn
import pytest


def test_alpha(): #проверка на лишние символы: буквы и тд
    with pytest.raises(SystemExit):
        calculator_rpn('45 2b +')

def test_empty_input(): #проверка на пустой ввод
    with pytest.raises(SystemExit):
        calculator_rpn(' ')

def test_int_division(): #проверка на целочисленную операцию
    with pytest.raises(SystemExit):
        calculator_rpn('55.0 51.8 //')

def test_big_number(): #проверка на возведение в степень больших чисел
    with pytest.raises(SystemExit):
        calculator_rpn('46464635484 65464846465 **')

def test_start_str(): #проверка на корректное начало строки с цифр или скобок
    with pytest.raises(SystemExit):
        calculator_rpn('+ 45 89 +')


def test_bracket(): #проверка на корректность выражений в скобках
    with pytest.raises(SystemExit):
        calculator_rpn('(8(4 5 + -))')

def test_wrong_bracket(): #проверка на корректность выражений в скобках
    with pytest.raises(SystemExit):
        calculator_rpn('2 )( 5 +')

def test_division_zero(): #деление на 0
    with pytest.raises(SystemExit):
        calculator_rpn('4 5 0 / +')


def test_correct_enter(): #проверка на корректный ввод: число операндов
    with pytest.raises(SystemExit):
        calculator_rpn('45 45 45')


def test_simple():
    assert calculator_rpn('45 2 +') == 47.0


def test_leading_decimal():
    assert calculator_rpn('.456555 .55 +') == 1.006555


def test_more_difficult_with_brackets():
    assert calculator_rpn('(4 9 5 * 2 4 - 2.0 ** / +)') == 15.25


def test_more_difficult():
    assert calculator_rpn('4 9 5 * 2 4 - 2.0 ** / +') == 15.25



def test_difficult():
    assert calculator_rpn('(45 8 +) 7 +') == 60
