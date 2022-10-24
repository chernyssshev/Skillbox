word = input("Введите слово: ")
letters = list(word)
letters_count = len(letters) - 1
new_word = []
for i in range(letters_count, -1, -1):
    new_word.append(letters[i])
if new_word == letters:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")
