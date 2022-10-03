import math

num = int(input('Введите кол-во чисел: '))

for i in range(num):
  x = float(input('Введите число: '))
  if x > 0:
    x = math.ceil(x)
    print('x =', x, '   log(x) =', math.log(x))
  else:
    x = math.floor(x)
    print('x =', x, '   exp(x) =', math.exp(x))