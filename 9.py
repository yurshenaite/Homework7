n, k, r = map(int, input().split())

def total_day(n, k, r):
    day = 1
    while n < r:
        n += n * (k / 100)
        day += 1
    return day

print(total_day(n, k, r))