import math

num = int(input('Введите число: '))
def is_square(num):
    root = math.isqrt(num)
    return root * root == num

if is_square(num) == True:
    print('Явяется полным квадратом')
else:
    print('Не является полным квадратом')
    num_2 = int(input('Введите другое число: '))
    while is_square(num_2) == False:
        num_2 = int(input('Введите другое число: '))
        if num_2 == True:
            break
    print('Является полным квадратом')