def task_1(a: int = 8, b: float = 10.5, c: str = 'stroka', d: list = [1, 2], f: bool = True) -> str:
    return type(a), type(b), type(c), type(d), type(f)


print(task_1())


def task_2(a=[1, 2, 3, 5, 8, 13, 21]) -> list:   # Фибоначчи
    return a[0:3]


print(task_2())


def task_3(x: int) -> int:
    return x**2


print(task_3(10))

