def min_num():
  num1 = int(input("Введите первое число: "))
  num2 = int(input("Введите второе число: "))
  
  print("Минимальное число:", round(((num1 + num2) - abs(num1 - num2)) / 2))

min_num()