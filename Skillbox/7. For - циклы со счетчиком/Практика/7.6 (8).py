for number in range(10, 100):
    digit1 = number // 10
    digit2 = number % 10
    if (digit1 * digit2 * 3 == number):
        print('Найдено замечательное число:', number)