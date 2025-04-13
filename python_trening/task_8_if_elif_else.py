num_float = 3.4

# Также попробуйте варианты
# num_float = 0
# num_float = -4.5

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

permit_print = True

if num_float > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')


def current_grade(n):
    if n > 0 and n <= 4:
        print('Бакалавр')
    elif n > 4 and n <= 6:
        print('Магистр')
    elif n > 6 and n <= 9:
        print('Аспирант')
    else:
        print('Введите корректный год обучения')

current_grade(6)


def number(n):
    if n > 100 or n < -100:
        print('-')
    else:
        print('+')

number(80)


class BasePage:
    def __init__ (self, driver, base_url):
        self.driver = driver
        self.base_url = base_url # 'https://demoga.com/'

    def visit(self):
        return self.driver.get (self.base_url)


class Page:
    def __init__ (self, url):
        self.url = url

    def visit(self):
        return driver.get(self.url)

home_page = Page('https://demoga.com/')