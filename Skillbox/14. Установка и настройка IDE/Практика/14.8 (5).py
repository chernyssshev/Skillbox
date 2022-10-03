def get_min_div(a):
    min_div = 1
    for i in range(1, a + 1):
        if a % i == 0:
            min_div = i
        if min_div > 1:
            break
    return min_div
 
number = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы:', get_min_div(number))
