first_list = []
second_list = []

for i in range(3):
    print(f'Введите число {i + 1}:', end = " ")
    first_number = int(input(""))
    first_list.append(first_number)

for i in range(7):
    print(f'Введите число {i + 1}:', end = " ")
    second_number = int(input(""))
    second_list.append(second_number)

print("Первый список: ", first_list)
print("Второй список: ", second_list)

first_list.extend(second_list)
for i in first_list:
    while first_list.count(i) != 1:
        first_list.remove(i)

print("Новый первый список с уникальными элементами: ", first_list)
