boys = int(input('Сколько мальчиков?: '))
girls = int(input('Сколько девочек?: '))
answer = ''
answer_one = ''

if (boys > girls * 2) or (boys * 2 < girls):
  print('Нет решения.')
elif boys > girls:
  k = boys - girls
  for bgb in range(k):
    answer += 'BGB'
  BG = girls - k
  for bg in range(BG):
    answer_one += 'BG'
elif boys < girls:
  k = girls - boys
  for gbg in range(k):
    answer += 'GBG'
  GB = boys - k
  for gb in range(GB):
    answer_one += 'GB'
print(answer + answer_one)