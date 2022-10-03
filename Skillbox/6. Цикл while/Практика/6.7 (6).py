est_pos = 0
est_neg = 0
while True:
  est = int(input('Введите оценку: '))
  if est > 0:
    est_pos += 1
  elif est < 0:
    est_neg += 1
  elif est == 0:
    break
print('Количество положительных оценок:', est_pos)
print('Количество отрицательных оценок:', est_neg)