suitable = 0
for counter in range(10):
    test_number = int(input(f'Введите {counter + 1}-е число: '))
    if(test_number > 0) and (test_number % 2 == 0):
        suitable += 1
print('Чётных и положительных чисел: ', suitable)