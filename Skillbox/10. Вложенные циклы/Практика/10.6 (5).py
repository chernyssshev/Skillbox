prime_numbers = int(input('Введите количество простых чисел: '))

for num in range(prime_numbers):
    number = int(input('Введите число: '))
    for step in range(2, number // 2 + 1):
        if number % step == 0:
            prime_numbers -= 1
            break
          
print('Количество простых чисел в последовательности: ', prime_numbers)