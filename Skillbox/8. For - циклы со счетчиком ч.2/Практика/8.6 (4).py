start = int(input('Введите начало отрезка: '))
end = int(input('Введите конец отрезка: '))
multiplicity = int(input('Введите кратность: '))

summ = 0
count = 0

for i in range(start, end +1):
    if i % multiplicity == 0:
        count += 1
        summ += i
if count == 0:
    print('Расчет невозможен, так как нет подходящих чисел')
else:
    print('Среднее арифметическое чисел: ', summ // count)