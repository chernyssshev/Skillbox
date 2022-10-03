hours = int(input('Введите время: '))
if (hours < 8) or (hours >= 22) or (10 <= hours < 12) or (hours == 14 or 18 <= hours < 20):
  print('Посылку получить нельзя')
else:
  print('Можно получить посылку')


hours = int(input('Введите время: '))
if 8 <= hours < 10 or 12 <= hours < 14 or 15 <= hours < 18 or 20 <= hours < 22:
  print('Можно получить посылку')
else:
  print('Посылку получить нельзя')