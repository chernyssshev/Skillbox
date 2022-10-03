square = int(input('Введите размер квадрата: '))

for row in range(1, square + 1):
  for col in range(1, square + 1):
    if col == row:
      print('^', end = '')
    elif col == -row + square + 1:
      print('^', end = '')
    else:
      print(' ', end = '')
  print('')