temperature = float(input("Введите температуру (введите 0 для завершения): "))
counter = 0
previous_temperature = None

while temperature != 0:
    if previous_temperature is not None and temperature < previous_temperature:
        count_decreased += 1
    previous_temperature = temperature
    temperature = float(input("Введите следующую температуру (введите 0 для завершения): "))

print(count_decreased)