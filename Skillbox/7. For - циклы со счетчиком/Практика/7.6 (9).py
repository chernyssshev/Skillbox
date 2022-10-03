last_ZP = 0
increase = drop = 0
for counter in range (1, 11):
    ZP = int(input(f'Введите {counter}-ю зарплату: '))
    if (ZP > last_ZP):
        increase += 1
    else:
        drop += 1
    last_ZP = ZP
    # print(increase, drop, last_ZP)
    
print('ЗП бухгалтера росла:', increase, 'мес, падала:', drop, 'мес')
if(drop > 0):
    print('Числа не по возрастанию, наблюдалось падение ЗП! Пора валить.')
else:
    print('Числа по ворастанию, ЗП постоянно растёт!')