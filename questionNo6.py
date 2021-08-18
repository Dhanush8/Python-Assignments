n = int(input('Enter the number of legs: '))  # n=number of legs of the polygon
print('\nPlease Enter Your Coordinates in Clockwise or Anticlockwise!')  # message to user
x = []  # x=list of x coordinates
y = []  # y=list of y coordinates
a = 1
while a <= n:
    b = x.append(input('Enter the x coordinate: '))
    c = y.append(input('Enter the y coordinate: '))
    a += 1
g = 0
h = 0
d = 0
while d < n-1:
    e = float(x[d])*float(y[d+1])
    f = float(y[d])*float(x[d+1])
    g += e  # g=sum of ( 𝑥1𝑦2, 𝑥2𝑦3, … . . , 𝑥𝑛−1𝑦𝑛 )
    h += f  # h=sum of ( 𝑦1𝑥2, 𝑦2𝑥3, … … . , 𝑦𝑛−1𝑥𝑛 )
    d += 1
g += float(x[n-1])*float(y[0])  # g + 𝑥𝑛𝑦1 = sum of ( 𝑥1𝑦2, 𝑥2𝑦3, … . . , 𝑥𝑛−1𝑦𝑛, 𝑥𝑛𝑦1 )
h += float(y[n-1])*float(x[0])  # h + 𝑦𝑛𝑥1 = sum of ( 𝑦1𝑥2, 𝑦2𝑥3, … … . , 𝑦𝑛−1𝑥𝑛, 𝑦𝑛𝑥1 )
i = ((g-h)**2)**(1/2)  # | g-h |
A = (1/2)*i  # area of the polygon ( (1/2) * | g-h | )
print('Area:', A)
