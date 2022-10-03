long = int(input('Введите длинну рамки: '))
width = int(input('Введите ширину рамки: '))

for rows in range(0, width):
  for col in range(0, long):
    if col == 0 or col == long -1:
      print('|', end = '')
    elif rows == 0 or rows == width -1:
      print('-', end = '')
    else:
      print(' ', end = '')
   
  print('')