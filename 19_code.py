import math

number = 6528
kmere = 8

ref = {0:"A", 1:"C", 2:"G", 3:"T"}

def numberToPattern(num, k):
    if k == 1:
        return ref[math.floor(num)]
    prefixIndex = num/4
    r = num%4
    symbol = ref[math.floor(r)]
    prefixPattern = numberToPattern(prefixIndex, k - 1)
    return(prefixPattern + symbol)

parse = numberToPattern(number, kmere)
print(parse)
fileout = open("19_sub.txt", 'wt')
fileout.write(parse)
fileout.close()