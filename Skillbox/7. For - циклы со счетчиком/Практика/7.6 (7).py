while True:
    a = int(input('Введите начало отрезка (а): '))
    b = int(input('Введите конец отрезка (b): '))
    if(a < b):
        break
    else:
        print('b должно быть больше a! Введите еще раз!')

summ_number = counter = 0
for number in range(a, b + 1):
    if(number % 3 == 0):
        summ_number += number
        counter += 1
print(f'Среднее арифметическое чисел из отрезка [{a},{b}], кратных числу 3, равно: ', summ_number / counter)