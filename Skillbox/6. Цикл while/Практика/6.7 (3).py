while True:
  numb = int(input('Введите число: '))
  second_numb = 0
  if numb == 0:
    second_numb = 1
  else:
    while numb != 0:
      second_numb += 1 
      numb //= 10
  print('Количество цифер в числе:', second_numb)