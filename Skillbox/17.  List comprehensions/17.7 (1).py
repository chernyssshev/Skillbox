vowels_list = ["а", "у", "о", "ы", "и", "э", "я", "ю", "ё", "е", "А", "У", "О", "Ы", "И", "Э", "Я", "Ю", "Ё", "Е"]
text = input("Введите текст: ")
vowels_list_in_text = [char for char in text if char in vowels_list]

print("Список гласных букв:", vowels_list_in_text)
print("Длина списка:", len(vowels_list_in_text))
