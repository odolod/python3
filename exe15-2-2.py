""" Возьмите любые 1-3 задания из прошлых домашних заданий. 
Добавьте к ним логирование ошибок и полезной информации. 
Также реализуйте возможность запуска из командной строки с передачей параметров.

3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
Используйте правило для проверки: 
“Число является простым, если делится нацело только на единицу и на себя”. 
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч. """

import sys
import logging

LOG_FILENAME = 'exe15-2-2.log'

logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def is_prime(num):
    if num < 2:
        raise ValueError
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

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

def get_result(num):
    try:        
        if is_prime(num):
            res = f'Число {num} является простым'
        else:
            res = f'Число {num} является составным'
    except ValueError:
         res = 'Введено 0 или 1'
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
                    if not (0 <= num <= 100000):
                        raise ValueError
                    break
                except ValueError:
                    logging.error('Некорректные параметры. Укажите целое число меньше 100000.')
                    print('Некорректные параметры. Укажите целое число меньше 100000.')
                    
            result = get_result(num)
            print(result)
            logging.info(result)
            display_new_logs()
    else:
        while True:
            try:
                num = int(input('Введите целое число: '))
                if not (0 <= num <= 100000):
                    raise ValueError
                break
            except ValueError:
                logging.error('Некорректные параметры. Укажите целое число меньше 100000.')
                print('Некорректный ввод. Введите целое число меньше 100000.')
        result = get_result(num)
        print(result)
        logging.info(result)
        display_new_logs()

if __name__ == '__main__':
    main()