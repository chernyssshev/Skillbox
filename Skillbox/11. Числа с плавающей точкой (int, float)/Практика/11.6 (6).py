print('Ввод:')
lower_bound = int(input('Нижняя граница: '))
upper_bound = int(input('Верхняя граница: '))
step = int(input('Шаг: '))

print('Вывод:')
print('C' , '\t', 'F')
  
for c_temp in range(lower_bound ,upper_bound, step):
  print(c_temp, '\t', round(c_temp*1.8 + 32))
if c_temp != upper_bound:
  print(upper_bound, '\t', round(upper_bound*1.8 + 32))