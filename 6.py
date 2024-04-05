total_followers = int(input())

extent = 1
for i in range(1, 100+1):
    extent *= 2
    if extent < total_followers:
        print(extent)
    else:
        break