from task_9_checks import Checks

class Input(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text


class Button(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text


class Title(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text


class Link(Checks):
    def __init__(self, loc, text):
        super().__init__(loc)
        self.loc = loc
        self.text = text

search = Input('test#input', 'input')
btn = Button('test#button', 'button')
title = Title('test#title', 'title')
link = Link('test#link', 'link')


print('Аргументы класса Input - ' + '\n' + search.loc + ', ' + search.text + '\n')
print('Аргументы класса Button - ' + '\n' +  btn.loc + ', ' + btn.text + '\n')
print('Аргументы класса Title - ' + '\n' + title.loc + ', ' + title.text + '\n')
print('Аргументы класса Link - ' + '\n' + link.loc + ', ' + link.text + '\n')

print(search.check_text())
print(btn.check_text())
print(title.check_text())
print(link.check_text())

