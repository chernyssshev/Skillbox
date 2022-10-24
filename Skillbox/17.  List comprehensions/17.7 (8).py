sticks = int(input('Количество палок: '))
throws = int(input('Количество бросков: '))
arr = [i for lst in[list(range(int(input(f'Бросок {i+1}. Сбиты палки с номера '))-1, int(input(f'по номер ')))) for i in range(throws)] for i in lst]
print(f"Результат: {''.join(['.I.' if i not in arr else '-' for i in range(sticks)])}")