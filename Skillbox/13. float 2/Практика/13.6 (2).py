def max_number(a, b, c):
    max_n = ((a + b) + abs(a - b)) // 2
    return (((max_n + c) + abs(max_n - c)) // 2)


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
print('Максимальное число из трех: ', max_number(a, b, c))