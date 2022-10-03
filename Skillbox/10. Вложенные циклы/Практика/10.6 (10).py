num = int(input('Введите число: '))
print()

for row in range(1, num + 1):
  for col in range(row):
    print(num - col, end = '')
  print('.' * ((num - row) * 2), end = '')
  for col in range(row, 0, -1):
    print(num - col + 1, end = '')
  print()