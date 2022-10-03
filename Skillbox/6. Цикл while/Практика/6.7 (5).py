numb = int(input('Введите номер билета: '))
luck_numb1 = (numb // 100000) + (numb // 10000 % 10) + (numb // 1000 % 10)
luck_numb2 = (numb % 1000 // 100) + (numb % 100 // 10) + (numb % 10)
while luck_numb1 == luck_numb2:
  print('Счастливый билет!')
  break
if luck_numb1 != luck_numb2:
  print('Не счастливый билет.')