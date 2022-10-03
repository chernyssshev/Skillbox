number = int(input('Введите число: '))
factorial = 1
for counter in range(2, number + 1):
    factorial *= counter
print(f'Факториал числа {number} равен', factorial)