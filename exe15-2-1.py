""" Возьмите любые 1-3 задания из прошлых домашних заданий. 
Добавьте к ним логирование ошибок и полезной информации. 
Также реализуйте возможность запуска из командной строки с передачей параметров.

2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. 
Дано a, b, c - стороны предполагаемого треугольника. 
Требуется сравнить длину каждого отрезка-стороны с суммой двух других. 
Если хотя бы в одном случае отрезок окажется больше суммы двух других, 
то треугольника с такими сторонами не существует. 
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним. """

import sys
import logging

LOG_FILENAME = 'exe15-2-1.log'

logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

def get_triangle_type(a, b, c):
    if a == b == c:
        return 'равносторонний'
    elif a == b or a == c or b == c:
        return 'равнобедренный'
    else:
        return 'разносторонний'

def read_log_file():
    try:
        with open(LOG_FILENAME, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f'Файл {LOG_FILENAME} не найден')

def display_new_logs():
    try:
        with open(LOG_FILENAME, 'r') as file:
            logs = file.readlines()
            for log in logs[-1:]:
                print(log)
    except FileNotFoundError:
        print(f'Файл {LOG_FILENAME} не найден')

def get_result(a,b,c):
    if check_triangle(a, b, c):
        triangle_type = get_triangle_type(a, b, c)
        res = f'Треугольник существует. Тип треугольника: {triangle_type}'
    else:
        res = 'Треугольник с такими сторонами не существует'
    return res

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'log':
            read_log_file()
            return
        else:
            try:
                a = float(sys.argv[1])
                b = float(sys.argv[2])
                c = float(sys.argv[3])
                if a <= 0 or b <= 0 or c <= 0:
                    raise ValueError
                result = get_result(a,b,c)
                print(result)
                logging.info(result)
                display_new_logs()
            except (IndexError, ValueError):
                logging.error('Некорректные параметры. Введите три положительных числа.')
                print('Некорректные параметры. Введите три положительных числа.')
    else:
        while True:
            try:
                a = float(input('Введите длину стороны a: '))
                if a <= 0:
                    raise ValueError
                break
            except ValueError:
                print('Некорректный ввод. Введите положительное число.')

        while True:
            try:
                b = float(input('Введите длину стороны b: '))
                if b <= 0:
                    raise ValueError
                break
            except ValueError:
                print('Некорректный ввод. Введите положительное число.')

        while True:
            try:
                c = float(input('Введите длину стороны c: '))
                if c <= 0:
                    raise ValueError
                break
            except ValueError:
                print('Некорректный ввод. Введите положительное число.')

        result = get_result(a,b,c)
        print(result)
        logging.info(result)
        display_new_logs()

if __name__ == '__main__':
    main()