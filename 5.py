volume_max = int(input())

for i in range(1, 100+1):
    if i ** 3 < volume_max:
        print((i ** 3), end=' ')
    else:
        break