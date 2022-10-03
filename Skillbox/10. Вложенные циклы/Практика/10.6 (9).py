size = int(input('Введите выcоту перамиды: '))
count = 1

for row in range(0, size + 1):
  print('\t' * (size - row), end = '')
  for col in range(row):
    print(count, end = '')
    count += 2
    print('\t'* 2, end = '')
  print()