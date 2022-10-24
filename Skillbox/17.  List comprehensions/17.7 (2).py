list_length = int(input("Введите длину списка: "))
list_number = list(range(list_length))
result = [num % 5 if list_number.index(num) % 2 != 0
               else 1 for num in list_number]
print("Результат:", result)
