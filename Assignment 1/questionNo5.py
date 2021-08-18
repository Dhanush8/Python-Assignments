N = int(input('N: '))
x = 1
Total = 0
while x <= N:
    Total += x
    x += 1
avg = Total/N
print('Average:', avg)
