def add_1(a: int, b: int) -> int:
    return max(a, b)


print(add_1(15, 100))


def add_2(a: int, b: int) -> str:
    if max(a, b) - min(a, b) == 135:
        result = 'Yes'
    else:
        result = 'No'
    return result


print(add_2(-140, -5))


def add_3(a: int) -> str:
    if a in range(1, 3) or a == 12:
        sizon = 'Зима'
    elif a in range(3, 6):
        sizon = 'Весна'
    elif a in range(6, 9):
        sizon = 'Лето'
    elif a in range(9, 12):
        sizon = 'Осень'
    else:
        sizon = 'Введите число от 1 до 12 включительно'
    return sizon


print(add_3(9))


def add_4(a: int, b: int, c: int) -> str:
    if a > 10 and b > 10 and c > 10:
        result = 'Yes'
    else:
        result = 'No'
    return result


print(add_4(9, 15, 11))


def add_5(a: list) -> int:
    result = 0
    for elem in a:
        if elem > 0:
            result += 1
    return result


print(add_5([1, 2, -3, -4, 5]))


def add_6(years: int, months: int) -> int:
    return 29 * months + 29 * 12 * years


print(add_6(0, 8))