count = 0

print('Раезмер конверта 12х12')
side = int(input('Введите размер письма (см.): '))
for i in range(side):
  if side > 12:
    count += 2
    side //= 2
print('Конверт нужно свернуть в', count, 'раз(а).')