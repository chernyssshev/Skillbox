first = int(input('Пробег(трехзначное число): '))

second = int(input('Номер дня: '))
a1 = first // 100 % 10 + first // 10 % 10 + first % 10 
if a1 > second:
  print('Сброс')
else:
  print('Сегодня не сломался')