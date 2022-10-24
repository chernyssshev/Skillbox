from distutils.command.build_scripts import first_line_re


number_list = [1, 4, -3, 0, 10]
result = []
last_number = len(number_list)
first_number = 3 #сдвиг
for i in range(last_number - first_number, last_number):
    result.append(number_list[i])
for i in range(0, last_number - first_number):
    result.append(number_list[i])
print("Сдвиг: ", first_number)
print("Старый список", number_list)
print("Новый список", result)
