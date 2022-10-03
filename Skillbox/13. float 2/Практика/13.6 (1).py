n = float(input('Введите число: '))
b = 0
if n < 1:
    while n < 1:
        n *= 10
        b -= 1
elif n >= 10:
    while n >= 10:
        n /= 10
        b += 1
print('Формат плавающей точки: x =', n, '* 10 **', b)