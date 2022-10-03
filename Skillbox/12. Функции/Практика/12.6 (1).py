def summa_n(n):
  summ = 0
  for num in range(n + 1):
    summ += num
  print(f'Я знаю, что сумма чисел от 1 до {n} равна {summ}')

n = int(input('Введите число: '))
summa_n(n)