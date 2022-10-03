import math


num1, num2 = int(input('Введите первое число: ')), int(input('Введите второе число: '))

def nod(num1, num2):
  print(f'Наибольший общий делитель двух чисел= {math.gcd(num1, num2)}')
  
nod(num1, num2)