start = int(input('Введите начало отрезка: '))
end = int(input('Введит конец отрезка: '))
step = int(input('Введите шаг: '))

if end > start and step < 0:
  for x in range(end, start - 1, step):
    y = x**3 + 2*x**2 - 4*x + 1
    print('В точке X='+ str(x),'|Y='+ str(y))
elif start > end and step > 0:
  for x in range(start, end-1, -step):
    y = x**3 + 2*x**2 - 4*x + 1
    print('В точке X='+ str(x),'|Y='+ str(y))
else:
  print('Введены некорректные значения')