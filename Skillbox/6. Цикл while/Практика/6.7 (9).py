n = 5
numb_of_attempts = 0
while True:
  numb = int(input('Введите число: '))
  if numb > n:
    print('Число больше чем нужно. Попробуйте ещё раз!')
    numb_of_attempts += 1
  elif numb < n:
    print('Число меньше, чем нужно. Попробуйте ещё раз!') 
    numb_of_attempts += 1
  elif numb == n:
    numb_of_attempts += 1
    print('Вы угадали! Число попыток: ', numb_of_attempts)
    break