class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height


rec1 = Rectangle(5, 6)
rec2 = Rectangle(12, 10)
rec3 = Rectangle(123, 258)

print(f'Прямоугольник №1: S = {rec1.area()}, P = {rec1.perimeter()}')
print(f'Прямоугольник №2: S = {rec2.area()}, P = {rec2.perimeter()}')
print(f'Прямоугольник №3: S = {rec3.area()}, P = {rec3.perimeter()}')
print('\n')


class Math:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def addition(self):
        print('a + b = ', self.a + self.b)

    def multiplication(self):
        print('a * b = ', self.a * self.b)

    def division(self):
        print('a / b = ', self.a / self.b)

    def subtraction(self):
        print('a - b = ', self.a - self.b)


calc1 = Math(5, 12)

calc1.addition()
calc1.multiplication()
calc1.division()
calc1.subtraction()
print('\n')


class Button:
    def __init__(self, text, type = 'Кнопка', loc = None):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        print(f'Клик по кнопке {self.text}')


text_box = Button('Text Box')
check_box = Button('Check Box')
radio_button = Button('Radio Button')
web_tables = Button('Web Tables')
buttons = Button('Buttons')
links = Button('Links')
broken_links = Button('Broken Links - Images')
upload_download = Button('Upload and Download')
dynamic_properties = Button('Dynamic Properties')

print('Текст кнопок: ', text_box.text, check_box.text, radio_button.text, web_tables.text, buttons.text, links.text, broken_links.text, upload_download.text, dynamic_properties.text, sep = ', ', end = '\n')
text_box.click()
check_box.click()
radio_button.click()
web_tables.click()
buttons.click()
links.click()
broken_links.click()
upload_download.click()
dynamic_properties.click()
