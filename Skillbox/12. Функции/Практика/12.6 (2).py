def test():
  num = int(input('Введите целое число: '))
  if num >= 0:
    positive()
  else:
    negative()

def positive():
  print('Положительное')

def negative():
  print('Отрицательное')

test()