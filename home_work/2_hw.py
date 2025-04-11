def task_1() -> tuple[str, str, str, str, str]:
    i: int = 3
    f: float = 7.5
    s: str = 'hello'
    l: list = [1, 7, 'world', 4.8, False]
    b: bool = True

    return str(type(i).__name__), str(type(f).__name__), str(type(s).__name__), str(type(l).__name__), str(type(b).__name__)

print(task_1())


def task_2() -> list:
    a = [1, 2, 3, 5, 8, 13, 21] #список
    return a[0:3] #срез списка

print(task_2())


def task_3(a: int) -> int:
    return a * a

print('Выод функции task_3 (квадрат числа) - ', task_3(3))