task_sum = 0
wife_sum = 0
hour = 1
print('Начался 8-часовой рабочий день')
while hour <= 8:
  print(hour, 'час')
  task = int(input('Сколько задач решит Максим? '))
  wife = int(input('Звонит жена. Взять трубку? (1-да, 0-нет) '))
  hour += 1
  task_sum += task
  wife_sum += wife
print('Рабочий день закончился. Всего выполнено задач: ', task_sum)
if wife_sum > 0:
  print('Нужно зайти в магазин')