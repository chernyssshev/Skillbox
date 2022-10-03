first = int(input(' Введите первое число '))
second = int(input(' Введите второе число '))
three = int(input('Введите третье число '))
if first > second:
  max = first
else:
  max = second 
if three > max:
  max = three
print(max)