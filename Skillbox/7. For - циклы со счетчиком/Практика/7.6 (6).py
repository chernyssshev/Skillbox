people_class = int(input('Сколько человек в классе? '))
mark3 = mark4 = mark5 = 0

for counter in range(1, people_class + 1):
    # --- Проверка корректности введенной оценки 
    flag = True
    while flag:
        mark = int(input(f'Оценка {counter}-го ученика: '))
        if (mark == 2):
            print('Двоек сегодня не ставили. Введите оценку еще раз!')         
        elif (mark != 3) and (mark != 4) and (mark != 5):
            print('Таких оценок не ставят! Введите еще раз!')
        else: 
            flag = False
    # ---
    if(mark == 3):
        mark3 += 1
    elif (mark == 4):
        mark4 += 1
    else:
        mark5 += 1
print('Отличников:', mark5, 'Хорошистов:', mark4, 'Троечников:', mark3)
if(mark5 > mark4) and (mark5 > mark3):
    print('Отличников сегодня больше!')
elif (mark4 > mark5) and (mark4 > mark3):
    print('Хорошистов сегодня больше!')
elif (mark4 == mark5) and (mark4 > mark3):
    print('Отличников и хорошистов поровну, по', mark4)
elif (mark4 == mark3) and (mark4 > mark5):
    print('Хорошистов и троечников поровну, по', mark4)
elif (mark5 == mark3) and (mark5 > mark4):
    print('Отличников и троечников поровну, по', mark5)
else:
    print('Троечников сегодня больше!')