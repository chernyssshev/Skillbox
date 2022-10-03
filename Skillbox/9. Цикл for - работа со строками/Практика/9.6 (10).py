x_word = input('Введите зашифрованное сообщение: ')

word_st = ''
word_fsh = ''
count = 0

for letter_st in (x_word):
  count += 1
  if count % 2:
    word_st += letter_st
  else:
    word_fsh += letter_st
    
print(word_st + word_fsh[::-1])