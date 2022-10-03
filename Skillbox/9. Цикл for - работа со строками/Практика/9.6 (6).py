string = input('Введите строку: ')
countLetter = 0
countLetterMax = 0

for letter in (string):
  if letter == 's':
    countLetter += 1
  else:
    countLetter = 0
  lastLetter = letter
  if countLetterMax < countLetter:
    countLetterMax = countLetter
print('Самая длинная последовательность:', countLetterMax)