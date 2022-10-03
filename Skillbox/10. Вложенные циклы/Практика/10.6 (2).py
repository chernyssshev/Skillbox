num = int(input('Введите число: '))

for rows in range(1, num + 1):
  for col in range(1, num + 1):
    if col <= rows:
      print(rows, end = '\t')
  print('') 