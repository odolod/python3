""" Возьмите любые 1-3 задания из прошлых домашних заданий. 
Добавьте к ним логирование ошибок и полезной информации. 
Также реализуйте возможность запуска из командной строки с передачей параметров.

Напишите программу, 
которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата. """

import sys
import logging

LOG_FILENAME = 'exe15-2-3.log'

logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

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

hex_literals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e', 'f']

def convert(num: int) -> str:
    res: str = ''
    while num > 0:
        res = str(hex_literals[num % 16]) + res
        num //= 16
    return res

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == 'log':
            read_log_file()
            return
        else:
            while True:
                try:
                    num = int(sys.argv[1])
                    if num < 0:
                        raise ValueError
                    break
                except ValueError:
                    logging.error('Некорректные параметры. Укажите целое число больше 0.')
                    print('Некорректные параметры. Укажите целое число больше 0.')
                    
            result = convert(num) + " = " + hex(num)[2:]
            print(result)
            logging.info(result)
            display_new_logs()
    else:
        while True:
            try:
                num = int(input('Введите любое целое число >0: '))
                if num < 0:
                    raise ValueError
                break
            except ValueError:
                logging.error('Некорректные параметры. Укажите целое число больше 0.')
                print('Некорректные параметры. Укажите целое число больше 0.')
                
        result = convert(num) + " = " + hex(num)[2:]
        print(result)
        logging.info(result)
        display_new_logs()

if __name__ == '__main__':
    main()