people_count = int(input("Кол-во человек: "))
number = int(input("Какое число в считалке? "))
print(f"Значит выбывает каждый {number}-й человек")

people_list = list(range(1, people_count + 1))

while len(people_list) > 1:
    print("Текущий круг людей:", people_list)
    begin_number = int(input("Начало счёта с номера "))
    count = people_list.index(begin_number)
    for i in range(number):
        count += 1
        if count == len(people_list):
            count = 0
    print("Выбывает игрок под номером", people_list[count - 1])
    people_list.remove(people_list[count - 1])

print("Остался человек под номером", people_list[0])
