v = int(input('Введите скорость (км/ч): '))
t = int(input('Введите время (ч): '))
s = v * t 
lap = s // 115
remains = s % 115
print ('Ответ:', lap, 'круг(а/ов)', remains, 'км')
