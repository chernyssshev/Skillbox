footer_length = int(input('Введите общую длину колонтитула в символах: '))
exclamation_mark = int(input('Введите количество восклицательных знаков: '))

footer_length_calc = round(footer_length / 2) - round(exclamation_mark / 2)
print('~' * footer_length_calc + '!' * exclamation_mark + '~' * footer_length_calc)