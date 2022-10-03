factorial_num = int(input('Введите число: '))

factorial = 1
summ = 0

for factorial_step in range(1, factorial_num + 1):
  factorial *= factorial_step
  summ += factorial
  
print('Сумма факториалов= ', summ)