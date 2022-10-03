cows = input('Введите строку из 10 символов a и b : ')

count = 0
milk = 0

for cow_stall in (cows):
  count += 1
  if cow_stall == 'b':
    milk += count * 2
    
print('Произведено молока за день:', milk)