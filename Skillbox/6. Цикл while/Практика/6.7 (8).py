deposit = int(input('Укажите сумму которая лежит в банке: '))
percent = int(input('Укажите под какой процент положили деньги в банк: '))
summ = int(input('Укажите какую сумму хотите накопить: '))
years = 0
while summ > deposit:
  deposit += percent * (deposit / 100)
  years += 1
print(years, 'лет потребуется, чтобы накопить желаемую сумму')