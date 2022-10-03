first = int(input('Первое число: '))
second = int(input('Второе число: '))
third = int(input('Третье число: '))

if first >= second and first >= third:
  print("Самое большое число:", first)
elif second >= first and second >= third:
  print("Самое большое число:", second)
else:
  print("Самое большое число:", third)