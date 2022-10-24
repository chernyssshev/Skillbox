word = input("Введите слово: ")
letters_of_word = list(word)
count_of_letters = len(letters_of_word)
unique_symbol = 0
count = 0
for index in range(count_of_letters):
    count = 0
    for sym in letters_of_word:
        if letters_of_word[index] == sym:
           count += 1
    if count >= 2:
        unique_symbol += 1


result = len(letters_of_word) - unique_symbol
print("Кол-во уникальных букв: ", result)
