sum_ = float(input('Введите сумму кредита: '))
year_ = int(input('На сколько лет выдан? '))
percent_ =  float(input('Сколько процентов годовых? ')) / 100
def payment(s, n, i):
        k = (i * (1 + i) ** n) / ((1 + i) ** n - 1)
        a = round(k * s, 2)
        return a
def specified_period(sum, percent, a, period):
        for q in range(1, period + 1):
                paid_percent = sum * percent
                paid_credit = a - paid_percent
                print('\nПериод: ', q)
                print('Остаток долга на начало периода: ', sum)
                print('Выплачено процентов: ', paid_percent)
                print('Выплачено тело кредита: ', paid_credit)
                sum -= paid_credit
        else:
                print('\nОстаток долга: ', sum)
        return sum
a_ = payment(sum_, year_, percent_)
new_sum_ = specified_period(sum_, percent_, a_, 3)
new_year_ = int(input('\nНа сколько лет продлевается договор? '))
new_percent_ = float(input('Увеличение ставки до: ')) / 100
new_year_ = new_year_ + (year_ - 3)
new_payment = payment(new_sum_, new_year_, new_percent_)
new_sum = specified_period(new_sum_, new_percent_, new_payment, new_year_)
