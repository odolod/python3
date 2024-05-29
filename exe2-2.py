""" Напишите программу, 
которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата. """

hex_literals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']

def get_number() -> int:
    num = input('Введите любое целое число >0: ')
    return int(num)

def convert(num: int) -> str:
    res: str = ''
    while num > 0:
        res = str(hex_literals[num % 16]) + res
        num //= 16
    return res


num = get_number()
if isinstance(num, int):
    print(convert(num))

print(hex(num)[2:])