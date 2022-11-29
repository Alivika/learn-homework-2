"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

from datetime import datetime
from datetime import date, timedelta


def print_days():
    dt_now = datetime.now()

    # Сегодня
    print(dt_now.strftime('%d.%m.%Y %H:%M'))

    # Вчера
    yesterday = datetime.now() - timedelta(days=1)
    print(yesterday.strftime('%d.%m.%Y %H:%M'))

    # 30 дней назад
    month_ago = datetime.now() - timedelta(days=30)
    print(month_ago.strftime('%d.%m.%Y %H:%M'))


def str_2_datetime(date_string):
    # Превратите строку "01/01/25 12:10:03.234567" в объект datetime

    date_str = '01/01/25 12:10:03.234567'
    date_dt = datetime.strptime(date_str, '%m/%d/%y %H:%M:%S.%f')
    return date_dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
