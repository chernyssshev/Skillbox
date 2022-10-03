month = 0 
while True:
  days = int(input('Введите колличество дней: '))
  if days == 0:
    break
  if days % 2 != 0:
    month += 1
print('Количество месяцев с четным количеством дней: ', month)