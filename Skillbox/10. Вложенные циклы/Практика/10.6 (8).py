height_triangle = int(input('Введите высоту треугольника: '))

count = 1

for row in range(0, height_triangle):
  for col in range(1, height_triangle - row):
    print(' ', end = '')
  print(count * '#', end = '')
  count += 2
  print()