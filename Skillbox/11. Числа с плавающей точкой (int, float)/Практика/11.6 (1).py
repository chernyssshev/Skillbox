euro = float(input('Введите стоимость покупки в евро: '))

dol = euro*1.25
rub = dol*60.87

print('Покупка будет стоить в рублях:', round(rub, 2))