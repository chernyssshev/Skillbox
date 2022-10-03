print('Введите местоположение коня:', )
loc_x = float(input(''))
loc_y = float(input(''))
loc_x = int(loc_x*10)
loc_y = int(loc_y*10)

print('Введите местоположение точки на доске:')
loc_point_x = float(input(''))
loc_point_y = float(input(''))
loc_x_point = int(loc_point_x*10)
loc_y_point = int(loc_point_y*10)

x_abs = abs(loc_x_point - loc_x)
y_abs = abs(loc_y_point - loc_y)

print('Конь в клетке ('+ str(loc_x) + ',' + str(loc_y) + '). Точка в клетке (' + str(loc_x_point) + ',' + str(loc_y_point) + ').')

if ((x_abs == 1) and (y_abs == 2)) or ((x_abs == 2) and (y_abs == 1)):
  print('Да, конь может ходить в эту точку.')
else:
  print('Конь не может ходить в эту точку')