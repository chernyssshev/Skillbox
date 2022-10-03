number_digits = int(input('Введите количествово чисел: '))
number_summ = 0
max_sum = 0
count_num = 0

for num in range(number_digits):
  count_num += 1
  print('Введите', count_num, '-ое число: ', end = '')
  number = int(input(''))
  number_1 = number
  while number > 0:
    number_summ += number % 10
    number //= 10
    if number_summ > max_sum:
      max_sum = number_summ
      number_max = number_1
  else:
    number_summ = 0

print()   
print('Наибольшее число по сумме цифр:', number_max, '\nСумма цифр:', max_sum)