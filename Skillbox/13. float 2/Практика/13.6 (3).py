def reverse(number):
    n = 0
    while number > 0:
        digit = number % 10
        number //= 10
        n *= 10
        n = n + digit
    return n
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print('Первое число наоборот: ', reverse(a))
print('Второе число наоборот: ', reverse(b))
sum_ = reverse(a) + reverse(b)
print('Сумма: ', sum_)
print('Сумма наоборот: ', reverse(sum_))