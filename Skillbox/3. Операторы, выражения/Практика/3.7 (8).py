a = int(input('Введите четырехзначное число: '))
first = a // 1000
second = a // 100 % 10
third = a // 10 % 10
fourth = a // 1 % 10
print (first, second, third, fourth)
