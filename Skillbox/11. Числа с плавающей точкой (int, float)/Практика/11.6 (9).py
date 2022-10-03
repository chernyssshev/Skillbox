import math


numb_a = float(input('Введите число а:'))
numb_b = float(input('Введите число b:'))
numb_c = float(input('Введите число c:'))

discriminant = numb_b ** 2 - 4*numb_a*numb_c
if discriminant > 0:
  radix_1 = - numb_b + (math.sqrt(discriminant))/ (2*numb_a)
  radix_2 = - numb_b - (math.sqrt(discriminant))/ (2*numb_a)
  print('В уравнении два корня: х1 = ', round(radix_1, 3), ', х2 = ', round(radix_2, 3))
elif discriminant == 0:
  radix = - numb_b / (2*numb_a)
  print('В уравнении один корень: x = ', radix)
else:
  print('В уравнении нет корней')