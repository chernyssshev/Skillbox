def factorial(num):
    f = 1
    for i in range(1, num +1):
        f *= i
    return f
precision = float(input('Введите точность: '))
x = int(input('Введите x: '))
n = 0
sum_ = 0
func = 1
while abs(func) > precision:
    func = (- 1) ** n * (x ** (2 * n) / factorial(2 * n))
    n += 1
    sum_ += func
print('Сумма ряда = ', sum_)