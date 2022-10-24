word = input('Введите строку: ')

reversed_fragment = word[word.find('h') + 1:word.rfind('h')]
word = reversed_fragment[::-1]

print(word)
