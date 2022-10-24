films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня', 'Шрек']
favorite_films = []
user_favorite_list = ""
while user_favorite_list != "end":
    user_favorite_list = input("Введите название фильма, поставьте точку если список закончен: ")
    if user_favorite_list in films:
        favorite_films.append(user_favorite_list)
    elif user_favorite_list == ".":
        break
    else:
        print("Такого фильма нет, или вы ввели с маленькой буквы")
print("Список любимых фильмов: ", favorite_films)
