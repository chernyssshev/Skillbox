income = int(input('Введите ваш доход: '))

if income < 10000:
  tax = income * 13 / 100
  print('Ваш налог:', tax)
elif 10000 <= income <= 50000:
  tax = (income - 10000) * 20 / 100 + (10000 * 13 / 100)
  print('Ваш налог:', tax)
else:
  tax = (income - 50000) * 30 / 100 + (50000 - 10000) * 20 / 100 + (10000 * 13 / 100)
  print('Ваш налог:', tax)