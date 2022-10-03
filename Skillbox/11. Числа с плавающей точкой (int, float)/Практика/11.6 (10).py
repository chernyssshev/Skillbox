num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

num_max = round(((num_1 + num_2) + abs(num_1 - num_2)) / 2)

print("Наибольшее число:", num_max)