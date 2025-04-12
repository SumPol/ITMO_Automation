class Input:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


class Button:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


class Title:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


class Link:
    def __init__(self, loc, text):
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

