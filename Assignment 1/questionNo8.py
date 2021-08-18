m = float(input('Enter the marks: '))  # m=marks
grade = ''
if m >= 93.33:
    grade = 'A'
elif m >= 90:
    grade = 'A-'
elif m >= 86.67:
    grade = 'B+'
elif m >= 83.33:
    grade = 'B'
elif m >= 80:
    grade = 'B-'
elif m >= 76.67:
    grade = 'C+'
elif m >= 73.33:
    grade = 'C'
elif m >= 70:
    grade = 'C-'
elif m >= 66.67:
    grade = 'D+'
elif m >= 63.33:
    grade = 'D'
elif m >= 60:
    grade = 'D-'
elif m >= 0:
    grade = 'F'
print('Grade:', grade)
