exp = int(input('Введите очки опыта: '))
if exp < 1000:
  print('Ваш уровень: 1')
elif exp >= 1000 and exp < 2500:
  print('Ваш уровень: 2')
elif exp >= 2500 and exp < 5000:
  print('Ваш уровень: 3')
else:
  print('Ваш уровень: 4')