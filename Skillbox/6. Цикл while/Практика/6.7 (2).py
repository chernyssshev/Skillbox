name = input('Введите имя должника: ')
summ = int(input('Введите сумму долга: '))
print(name, 'ваша сумма долга', summ, 'рублей.')
while True:
  debt = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? '))
  if debt < summ:
    print('Маловато,', name,'. Накиньте ещё деньжат.')
  elif debt >= summ:
    print('Отлично,', name,'! Вы погасили долг. Спасибо.')
    break