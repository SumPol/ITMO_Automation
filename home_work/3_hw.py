def bigger_num(a, b):
    if a > b:
        print('Первое число больше второго - ', a)
    else:
        print('Второе число больше первого - ', b)

bigger_num(float(input('Введите первое число ')), float(input('Введите второе число ')))


def diff_135(a, b):
    if a - b == 135 or a - b == -135:
        print('Yes')
    else:
        print('No')

diff_135(float(input('Введите первое число ')), float(input('Введите второе число ')))


def season(n):
    if n in (12, 1, 2):
        print('Зима')
    elif n in (3, 4, 5):
        print('Весна')
    elif n in (6, 7, 8):
        print('Лето')
    elif n in (9, 10, 11):
        print('Осень')
    else:
        print('Такого месяца нет')

season(int(input('Введите номер месяца от 1 до 12 ')))


def more_then_10(a, b, c):
    if a > 10 and b > 10 and c > 10:
        print('Yes')
    else:
        print('No')

more_then_10(float(input('Введите первое число ')), float(input('Введите второе число ')), float(input('Введите третье число ')))


# Число 0 не является ни положительным, ни отрицательным числом
def positive_nums(a):
    counter = 0
    for num in a:
        if num > 0:
            counter += 1
    print('Кол-во положительных чисел ', counter)

positive_nums(float(input()) for i in range(5))


def days_in_period(years: int, months: int, days: int = 29):
    print('Кол-во дней за указанный период: ', (years * 12 + months) * days)

days_in_period(int(input('Введите кол-во лет ')), int(input('Введите кол-во месяцев ')))