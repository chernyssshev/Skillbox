def reverse(num):
  text = ''
  while num > 0:
    last_num = str(num % 10)
    text += last_num
    num = num // 10
  reverse_num = int(text)
  print('Число наоборот:', reverse_num)

while True:
  num = int(input('Введите число: '))
  if num !=0:
    reverse(num)
  else:
    print('Программа завершена!')
    break