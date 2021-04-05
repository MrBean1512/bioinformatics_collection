f = open('5_input.txt', 'r')
i = 0
for l in f:
    i += 1
    if (i%2 == 0):
        print(l, end='')
