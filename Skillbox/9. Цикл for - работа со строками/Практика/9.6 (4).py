number_rows = int(input('Введите количество рядов: '))
number_seats = int(input('Введите количество сидений в ряде: '))
number_meters = int(input('Введите количество метров между рядами: '))

print('\nСцена')

for i in range(number_rows):
  print('=' * number_seats, '*' * number_meters, '=' * number_seats)