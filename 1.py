counter = 0
for i in range(100, 999+1):
    if i % 17 == 0:
        counter += 1
        print(i, end=' ')

print(counter)