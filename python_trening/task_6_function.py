# # определяем функцию
# def add(x, y) :
#     return x + y
#
#
# # вызываем функцию
# print(add (1, 2))
#
# print(add('I a', 'm tester'))


# def arg(a, b, c=2, d=3):
#     return a + b + c + d
# print (arg(1, 1, 1, 1))
# print (arg(2, 2))
# print (arg(2, 2, '1',1))


# def range_arg (a, b, c, d):
#     return a + ' ' + b + ' ' + c + ' ' + d
#
# print (range_arg('1', '2', '3', '4'))
#
# print (range_arg('1','2', d='3', c='4'))

def tuple_f(a = (1, 2, 3, 4)):
    return a[1]

print(tuple_f((3, 4, 5, 6)))


def pl(radius, pi = 3.14159):
    return pi * radius * radius

print(pl(3))