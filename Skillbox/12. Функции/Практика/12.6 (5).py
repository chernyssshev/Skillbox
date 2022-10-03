def count_letters():
  text = input('Введите текст: ')
  num_user = input('Какую цифру ищем? ')
  letter_user = input('Какую букву ищем? ')
  
  count_letter = 0
  count_num = 0
  
  for sym in text:
    if sym == letter_user: 
      count_letter += 1
    if sym == num_user:
      count_num += 1
  print(f'Количество цифр {num_user}: {count_num}\nКоличество букв {letter_user}: {count_letter}')
  
count_letters()