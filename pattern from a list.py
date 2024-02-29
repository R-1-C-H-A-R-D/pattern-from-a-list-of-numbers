numbers = [3, -2, 5, -1, 4]

for i in numbers:
    pattern = ''
    if i < 0 :
        for test in range (abs(i)):
            pattern += 'o'
    else:
        for test in range (i):
            pattern += 'x'
    print (pattern)