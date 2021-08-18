i = str(input('Enter the Unit of Value(cm/m): '))  # i=input unit
x = float(input('Enter the value: '))  # x=input value
if i == 'cm':
    i = 0.393701*x  # i=inches
    f = i/12  # f=feets
    y = 0.0109361*x  # y=yards
    print('')
    print('Inches:', i)
    print('Feet:', f)
    print('Yards:', y)
elif i == 'm':
    i = 0.393701*x*100
    f = i/12
    y = 0.0109361*x*100
    print('')
    print('Inches:', i)
    print('Feet:', f)
    print('Yards:', y)
else:
    print('Please Enter the Correct Unit and Try Again!')
