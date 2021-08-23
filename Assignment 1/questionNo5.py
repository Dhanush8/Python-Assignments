N = int(input('N: '))
x = 1
Total = 0
count=0
while x <= N:
    Total += x
    count += 1
    x += 1
avg = Total/count
print('Average:', avg)
