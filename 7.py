answer = int(input('Введите ответ: '))

def check(answer):
    while answer % 2 == 0:
        answer /= 2
    return answer

if check(answer) == True:
    print('верно')
else:
    print('неверно')