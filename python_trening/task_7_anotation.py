a: int = 5
b: str = 'строка'
c: list = [1, 2]


def indent(s: str, width: int) -> str:
    return ' ' * (max(0, width - len(s))) + s


print(indent('123', 123))


def lingth(s: str='') -> int:
    return len(s)


print(lingth('stroka'))


def spisok(a: list, b: list) -> int:
    return max(len(a), len(b))


print(spisok([1, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
