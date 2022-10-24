number_list = [1,2,3,0,4,77,2,3,0,2,0,3,0,5,0,7,0,1,0,0,1,0]
print("Изначальный список:", number_list)

new_number = [number for number in number_list if number != 0]
print("Список в той же последовательности, но без нулей:", new_number)

new_number[len(new_number):] = [0] * number_list.count(0)
print("Список с 0 в конце:", new_number)