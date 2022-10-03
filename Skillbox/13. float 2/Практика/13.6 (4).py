text = input('Введите число в экспотенциальной форме: ')
m = ''
b = ''
flag = True
for i in text:
    if i == 'e' or i == 'E':
        flag = False
    elif flag:
        m += i
    else:
        b += i
print(m, b)