ur_wallet = int(input("Введите состояние счёта: "))
course_price = 75000

if ur_wallet >= course_price:
    ur_wallet -= course_price
    print("Курс успешно приобретён!")
else:
    print("Не хватает денег на счету")

print("Хорошего дня!")