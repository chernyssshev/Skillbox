def rock_paper_scissors(score):
  print('За победу +1 очко. Проигрыш -2 очко\n1. Камень\n2. Ножницы\n3. Бумага\n0. Вернуться в главное меню')
  choise_user = int(input('Что выбераете? '))
  choise_comp = random.randint(1, 3)
  
  if 0 <= choise_user <= 3: 
    if choise_user == 0:
      print()
      mainMenu(score)
    elif choise_comp == 1:
      print('Компьютер выбрал- Камень.')
    elif choise_comp == 2:
      print('Компьютер выбрал- Ножницы')
    elif choise_comp == 3:
      print('Компьютер выбрал- Бумагу')
     
    if choise_user == choise_comp:
      print('Ничья\n')
      rock_paper_scissors(score)
    elif (choise_comp == 1 and choise_user == 2) or (choise_comp == 2 and choise_user == 3) or (choise_comp == 3 and choise_user == 1):
      print('Вы проиграли!\n')
      score -= 2
      rock_paper_scissors(score)
    elif (choise_comp == 1 and choise_user == 3) or (choise_comp == 2 and choise_user == 1) or (choise_comp == 3 and choise_user == 2):
      print('Вы выйграли!\n')
      score += 1
      rock_paper_scissors(score)
  else:
    print('Некорректный выбор. Попробуйте ещё раз\n')
    rock_paper_scissors(score)

    
def guess_the_number(score):
  choise_comp = random.randint(1, 100)
  print('0. Возврат в главное меню\n1. Правила\n2. Начать игру')
  choise_user = int(input())
  
  if 0 <= choise_user <=2:
    if choise_user == 0:
      print()
      mainMenu(score)      
    elif choise_user == 1:
      print('\nПравила игры "Угадай число"\nКомпьютер загадывает число (от 1 до 100). Игрок должен отгадать за 7 попыток. Если игрок угадывает за меньше количество попыток, то игрок получает + 10 очков. Если же игрок проигровает, то - 20 очков.\n')
      guess_the_number(score)      
    elif choise_user == 2:    
      for attempts in range(7, 0, -1):
        print(f'\nПопытка №{attempts}\nКакое число загадал компьётер?', end =' ')
        num_user = int(input())
        if num_user > choise_comp:
          print('Моё число меньше')
        elif num_user < choise_comp:
          print('Моё число больше')
        else:
          print('Ты угадал! +10 очков\n')
          score += 10
          guess_the_number(score)
      print('Ты проиграл! -10 очков\n')
      score -= 20
      guess_the_number(score)
  else:
    print('Некорректный выбор. Попробуйте ещё раз\n')
    guess_the_number(score)


def mainMenu(score):
  print('Выберете игру\n1. Камень, ножницы, бумага\n2. Угадай число\n3. Мои очки\n4. Выйти из игры')
  choise = int(input())
  
  if choise == 1:
    print()
    rock_paper_scissors(score)
  elif choise == 2:
    print()
    guess_the_number(score)
  elif choise == 3:
    print(f'Ваши очки: {score}\n')
    mainMenu(score)
  elif choise == 4:
    print('Всего хорошего')
  else:
    print('Некорректный выбор. Попробуйте ещё раз\n')
    mainMenu(score)
  

import random

score = 50
mainMenu(score)