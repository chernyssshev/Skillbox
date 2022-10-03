from unittest import result


a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
d = int(input('Введите четвертое число: '))
result = 2 * (c + 5 + (a * b) / (4 * b)) * (d - 2 * (a ** 3 / 30)) - 10
print ('Ответ: ', result)
