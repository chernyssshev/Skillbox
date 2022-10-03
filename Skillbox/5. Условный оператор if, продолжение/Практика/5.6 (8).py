flat_area = int(input('Введите площадь квартиры: '))
flat_price = int(input('Введите цену квартиры (млн): '))
if flat_area >= 100 and flat_price <= 10 or flat_area >= 80 and flat_price <= 7:
  print('Квартира подходит!')
else:
  print('Квартира не подходит. Надо искать дальше.')