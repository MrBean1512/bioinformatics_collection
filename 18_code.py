text = "CTGCGTGCGAACGCCGTAACGACCCGAAT"

ref = {"A":0, "C":1, "G":2, "T":3}

def patternToNumber(pattern):
    if pattern == "":
        return 0
    symbol = pattern[-1]
    prefix = pattern[0:-1]
    # print(symbol + " " + prefix + " " + str(ref[symbol]))
    return 4 * patternToNumber(prefix) + ref[symbol]

parse = str(patternToNumber(text))
print(parse)
fileout = open("18_sub.txt", 'wt')
fileout.write(parse)
fileout.close()