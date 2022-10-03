total_ZP = 0
for counter in range (1, 13):
    ZP = int(input(f'Введите {counter}-ю зарплату: '))
    total_ZP += ZP
print('Средняя зарплата сотрудника: ', total_ZP / 12)