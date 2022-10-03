text = input('Введите текст: ')
count = 0
count_max = 0

for letter in (text):
  if letter != ' ':
    count += 1
  else:
    count = 0
  if count_max < count:
    count_max = count
    
print('Самое длинное слово, букв: ', count_max)