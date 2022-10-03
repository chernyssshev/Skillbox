a = int(input('Введите четырехзначное число: '))
first = a // 1000
second = a // 100 % 10
third = a // 10 % 10
fourth = a // 1 % 10
print ('Обратное:', fourth * 1000 + third * 100 + second * 10 + first)
