number_user = int(input('Введите натуральное число N: '))

summ = 0

for n in range(number_user + 1):
	x = (( - 1)**n)*(1/(2**n))
	summ += x
print('Член ряда =', x, '. Сумма ряда = ', summ)