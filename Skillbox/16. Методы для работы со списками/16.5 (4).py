guests_list = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
answer = ""
while answer != "Пора спать":
    print(f"Сейчас на вечеринке {len(guests_list)} человек", guests_list)
    answer = input("Гость пришел или ушел? ")
    if answer != "Пора спать":
        name = input("Имя гостя: ")
    if answer == "ушел":
        print(f"Пока, {name}!")
        guests_list.remove(name)
    if len(guests_list) >= 6:
        print(f"прости {name}, но мест нет")
    else:
        if answer == "пришел":
            print(f"Привет {name}!")
            guests_list.append(name)

print("Вечеринка закончилась, все легли спать.")
