
#В примере первый пример некорректный по условию 
#UPD: Со вторым все нормально 

friends_count = int(input("Кол-во друзей: "))
credit = int(input("Долговых расписок: "))

friends_list = []
for number in range(friends_count):
    friends_list.append([number, 0])

for credit_number in range(credit):
    print(f"{credit_number + 1} расписка")
    to_whom = int(input("Кому: "))
    from_whom = int(input("От кого: "))
    how_many = int(input("Сколько "))
    friends_list[to_whom - 1][1] -= how_many
    friends_list[from_whom - 1][1] += how_many

    print("Баланс друзей:")
    for index in range(friends_count):
        print(f"{(friends_list[index][0]) + 1} : {friends_list[index][1]}")
