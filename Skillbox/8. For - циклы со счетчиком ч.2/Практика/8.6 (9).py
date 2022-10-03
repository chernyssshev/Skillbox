x = (int(input('Введите число: ')))
numer = 1
denom = 1
for n in range(1, 7):
	prod_num = (x - (2**n - 1))
	numer *= prod_num
	prod_denom = (x - 2**n)
	denom *= prod_denom
print('числитель = ', numer, 'знаменатель = ', denom)
if denom == 0:
	print('На ноль делить нельзя!')
else:
	print('Результат = ', round(numer / denom, 4))