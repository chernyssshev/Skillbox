number_count = int(input('Кол-во чисел: '))
number_list = []
 
for i in range(number_count):
    number_list.append(int(input('Число: ')))
 
counter = 0
while number_list != number_list[::-1]:
    number_list.insert(number_count, number_list[counter])
    counter += 1
 
print('Нужно приписать чисел:', counter)
print('Сами числа:', number_list[:counter][::-1])
