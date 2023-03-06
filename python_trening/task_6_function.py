def add(x, y):
    return x + y

# вызываем функцию
print(add(1,2))

# вызываем функцию с другими аргументами
print(add('I a', 'm tester'))


def arg(a, b, c=2, d=3):
    return a + b + c + d


print(arg(1,1,1,1))

print(arg(2,2))

print(arg(2, 2, 1, 1))

def range_arg(a, b, c, d):
    return a + ' ' + b + ' ' + c + ' ' + d

print(range_arg('1', '2', '3', '4'))

print(range_arg('1', '2', d='3', c='4'))


a = (1, 2, 3, 4)


def zadacha_1(a):   # a=(1, 2, 3, 4)
    return a[0]


print(zadacha_1(a))


def zadacha_2(radius, pi=3.14159):
    return pi * radius**2


print(zadacha_2(10))
