man1 = int(input('Кубик Кости: '))
man2 = int(input('Кубик владельца: '))
check = man1 + man2
print('Сумма: ', check)
if man1 < man2: 
  print('Владелец платит')
if man1 >= man2:
  print('Костя платит')