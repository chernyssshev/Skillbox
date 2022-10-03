educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы на проживание: '))

income  = 0
difference = 0

for month in range(1, 11):
  income  = income + educational_grant
  if month >= 2:
    expenses += expenses * 0.03
  difference += expenses
need_money = round(difference- income, 3)
print('У родителей необходимо попросить:', need_money)