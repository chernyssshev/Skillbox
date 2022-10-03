violation = 0
for sector in range (30, 36):
    amount_people = int(input(f'Людей в {sector} секторе: '))
    if(amount_people <= 10):
        print('Всё спокойно.')
    else:
        violation += 1
        print('Нарушение! Слишком много людей в секторе!')
print('Всего нарушений: ', violation)