start_amplitude = float(input('Введите начальную амплитуду: '))
finish_amplitude = float(input('Введите амплитуду остановки: '))
count = 0
while start_amplitude > finish_amplitude:
    start_amplitude = start_amplitude - (start_amplitude * 8.4) / 100
    count += 1
print('Маятник считается остановимшися через ', count, 'колебаний')