N = int(input('Введите количество карточек всего: '))

total_summ = total_card = 0
for counter in range (1, N + 1):
    total_summ += counter
    if counter < N:
        card = int(input('Введите номер оставшейся карточки: '))
        total_card += card
print('Номер потерянной карточки: ', total_summ - total_card)