# a: int = 5
# b: str = 'строка'
# c: list = [1, 2]
#
# def indent(s: str, width: int) -> str:
#     return " " * (max(0, width - len(s))) + s
#
# print(indent('123', 123))


# def str_len(s: str) -> int:
#     return len(s)
#
# print(str_len('abcdefg'))


# def lists(a: list, b: list) -> int:
#     return max(len(a), len(b))
#
# print(lists([1, 2, 3, 4, 5], [9, 8, 7]))

# def lists(a: list, b) -> list:
#     a.append(b)
#     return a
#
# print(lists([1, 2, 3, 4, 5], 'hi'))


def lists(a: list) -> int:
    return sum(a)

print(lists([1, 2, 3, 4]))