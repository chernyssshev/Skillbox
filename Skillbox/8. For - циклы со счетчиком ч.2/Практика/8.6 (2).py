summ = 0

number_of_debt = int(input('Введите количество должников: '))

for number_of_debt in range(0, number_of_debt, 5):
  print('Должник с номером: ', number_of_debt)
  debt = int(input('Сколько должны? '))
  summ += debt
  print()
print('Общая сумма долга:', summ)