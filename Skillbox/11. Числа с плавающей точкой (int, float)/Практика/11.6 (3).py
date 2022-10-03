size_file = float(input('Укажите размер файла для скачивания: '))
conn_speed = float(input('Какова скорость вашего соединения? '))

time_download = round(size_file/conn_speed)
download = 0
percent = 0

for time in range(1, time_download + 1):
  download += conn_speed
  percent = round(download/size_file*100)
  if time == time_download:
    download = size_file
    percent = 100
  print('Прошло', time, 'сек. Скачано', round(download), 'из', round(size_file), 'Мб', '(' + str(percent) + '%)')