list = int(input('Введите место в списке: '))
scores = int(input('Введите количество баллов: ')) 
if scores >= 290 and list < 10:
  print('Поздравляем, вы поступили!')
  print('Бонусом вам будет начисляться стипендия.')
elif scores < 290 and list < 10:
  print('Поздравляем, вы поступили!')
  print('Но вам не хватило баллов для стипендии.')
else:
  print('К сожалению, вы не поступили.')