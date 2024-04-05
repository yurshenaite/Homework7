import math

num = int(input('Введите число: '))

def guess_num(num):
    return math.ceil(math.log2(num))

print(guess_num(num))