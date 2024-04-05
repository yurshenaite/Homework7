text = input('Введите строку: ')
total_text = ''

for i in range(len(text)):
    if i % 2 == 0:
        total_text += text[i]

print(total_text)