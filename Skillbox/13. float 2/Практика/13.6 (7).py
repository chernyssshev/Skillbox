depth_min = 0
depth_max = 4
danger_max = float(input('Введите максимальный уровень опасности: '))
depth = depth_min + (depth_max - depth_min) / 2
danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
if danger_max <= 0:
    print('Ошибка. Максимально допустимый уровень опасности должен быть больше нуля.')
else:
    #print('Глубина ', depth, 'Опасность ', danger)
    while abs(danger) > danger_max:
        if danger > 0:
            depth_min = depth
        else:
            depth_max= depth
        depth = depth_min + (depth_max - depth_min) / 2
        danger = depth ** 3 - 3 * depth ** 2 - 12 * depth + 10
        #print('Глубина ', depth, 'Опасность ', danger)
    print('Приблизительная глубина безопасной кладки: ', depth)
