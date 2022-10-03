first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
sum_number = int(input("Сумма этих чисел: "))

result_sum = first_number+second_number

if result_sum == sum_number:
    print("Ответ верный!")
else:
    print("Ответ неверный! Правильный ответ - ", result_sum)
