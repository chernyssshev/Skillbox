reverse_timer = int(input('Введите время для разогрева: '))

for reverse_timer in range(reverse_timer, 0, -1):
  readiness = int(input('Готовы лы Вы забрать еду (1-да, 0-нет): '))
  if readiness == 1:
    print('Ваша еда готова, можете забрать. До окончания программы осталось', reverse_timer, 'сек.')
    break
if reverse_timer == 1:
  print('Ваша еда готова, осторожно горячo!')