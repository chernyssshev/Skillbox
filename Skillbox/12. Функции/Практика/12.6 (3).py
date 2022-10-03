def calc():
  action = int(input('Выберите действие:\n1 - вывести сумму цифр числа\n2 - вывести максимальную цифру числа\n3 - вывести минимальную цифру числа\n'))
  if action == 1:
    summ()
    print()
    calc()
  elif action == 2:
    max_num()
    print()
    calc()
  else:
    min_num()
    print()
    calc()

def summ():
  num = int(input('Введите число: '))
  summ_num = 0
  while num > 0:
    summ_num += num % 10
    num = num // 10
  print(f'Сумма цифр числа равна {summ_num}') 

def max_num():
  num = int(input('Введите число: '))
  max_numb = num % 10
  while num > 0:
    num = num // 10
    if max_numb < num % 10:
      max_numb = num % 10
  print(f'Максимальная цифра в числе равна {max_numb}')

def min_num():
  num = int(input('Введите число: '))
  min_numb = num % 10
  while num > 0:
    num = num // 10
    if num == 0:
      break
    if min_numb > num % 10:
      min_numb = num % 10
  print(f'Минимальная цифра в числе равна {min_numb}')