def reverse(num, count):
    last_digit = num % 10
    first_digit = num // 10 ** (count - 1)
    between_digits = num % 10 ** (count - 1) // 10
    num = last_digit * 10 ** (count - 1) + between_digits * 10 + first_digit
    return num
def first_number():
    first_n = int(input('Введите первое число: '))
    first_num_count = 0
    temp = first_n
    while temp > 0:
        temp //= 10
        first_num_count += 1
    if first_num_count < 3:
        print("В первом числе меньше трёх цифр.")
    else:
        num = reverse(first_n, first_num_count)
        print('Измененное число: ', num)
        return num
def second_number():
    second_n = int(input('Введите второе число: '))
    second_num_count = 0
    temp = second_n
    while temp > 0:
        second_num_count += 1
        temp = temp // 10
    if second_num_count < 4:
        print("Во втором числе меньше четырёх цифр.")
    else:
        num = reverse(second_n, second_num_count)
        print('Измененное число: ', num)
        return  num
first = first_number()
second = second_number()
print('Сумма чисел: ', first + second)