today = input('Введите день недели: ')
countDay = 0

for day in ('понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресение'):
  countDay += 1
  if today == day:
    break
    
print('Номер дня недели: ', countDay)