num1 = 1
num2 = 100
attempts = 1
print('Загадайте число от 1 до 100')
while True:
  print(attempts,'- я попытка')
  num = (num1 + num2) // 2
  print('Вы загадали число', num, '?')
  solution = int(input('Ваше число: 1 — равно, 2 — больше, 3 — меньше. '))
  if solution == 1:
      break
  if solution == 2:
      num1 = num + 1 
  if solution == 3:
      num2 = num -1 
  attempts += 1
print('Загаданное вами число', num, 'потрачено ', attempts, 'попыток')