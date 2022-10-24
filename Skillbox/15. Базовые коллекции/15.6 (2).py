names_list = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
first_day = []
for i in range(0, len(names_list) - 1, 2):
    first_day.append(names_list[i])
print('Первый день:', first_day)
