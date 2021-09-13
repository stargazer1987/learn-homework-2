from datetime import date, datetime, timedelta
"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
dt_now = datetime.now()
delta = timedelta(days=1)
delta2 = timedelta(days=30)
yesterday = dt_now - delta
days_ago_30 = dt_now - delta2

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(f'Вчера: {yesterday}',f'Сегодня: {dt_now}',f'30 дней назад: {days_ago_30}',sep='\n')
    


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    return datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')

if __name__ == "__main__": 
    print_days()
    print(f'Перевод строки в дату: {str_2_datetime("01/01/20 12:10:03.234567")}')
