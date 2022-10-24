skates = []
foot_size = []
count = 0

skates_count = int(input('Кол-во коньков: '))
for i in range(skates_count):
    skates_number = 'Размер ' + str(i + 1) + ' пары: '
    size = int(input(skates_number))
    skates.append(size)

people_count = int(input('\nКол-во людей: '))
for i in range(people_count):
    people_number = 'Размер ноги ' + str(i + 1) + ' человека: '
    size = int(input(people_number))
    foot_size.append(size)
 
for i in foot_size:
    if i in skates:
        skates.remove(i)
        count += 1

print('Наибольшее кол-во людей, которые могут взять ролики:', count)

