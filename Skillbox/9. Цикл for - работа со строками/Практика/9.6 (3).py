message = input('Введите текст: ')
count_letter = 0
sym = False

for letter in (message):
  count_letter += 1
  if letter == '*':
    sym = True
    print('Символ ‘*’ стоит на позиции ', count_letter)
    break
if sym != True:
  print('Символ ‘*’ в тексте не встречается')