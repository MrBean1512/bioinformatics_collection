import itertools

file = open("21_input.txt", 'r')
lines = []
for line in file:
    lines.append("{}".format(line.strip()))
file.close()

k = int(lines[0].split()[0])
d = int(lines[0].split()[1])
dnaList = lines[1::]

# this is the main function
# find all kmere patterns with up to d mistakes that are shared by set of dna
def motifEnumeration(dnaList, k, d):

    # create all possible patterns with up to d mistakes
    allPatterns = []
    for dna in dnaList:
        patterns = []
        for kmere in range(0, len(dna) - k + 1):
            count = 0
            neighbors = genDNeighbors(dna[kmere:kmere+k], d) # generate all the d-neighbors
            for i in neighbors:
                patterns.append(i)
        allPatterns.append(patterns)
    
    # iterate through the lists of patterns and make a new list of all the patterns that each list has in common
    sharedPatterns = []
    for patternList in allPatterns:
        for pattern in patternList:
            count = 0
            for dnaCheck in allPatterns:
                if pattern in dnaCheck:
                    count += 1
            if count >= len(allPatterns):
                if pattern not in sharedPatterns:
                    sharedPatterns.append(pattern)
    
    return sharedPatterns

# generate all the nighbors of a given kmere with up to d mistakes
def genDNeighbors(text, d):

    allCombos = [ ''.join(l) for l in itertools.product("ACTG", repeat = d) ]
        # create all possible combinations of letters 
    allIndexes = [ l for l in itertools.combinations(range(len(text)), d) ]
        # create all possible combinations of indexes

    neighborhood = []
    for indexes in allIndexes:
        for combos in allCombos:
            temp = list(text)
            for i in range(0, d):
                temp[indexes[i]] = combos[i]
            if ''.join(temp) not in neighborhood:
                neighborhood.append(''.join(temp))

    return(neighborhood)



# parse and print the most frequent kmeres
solution = motifEnumeration(dnaList, k, d)
parse = " ".join(str(x) for x in solution)
print(parse)
fileout = open("21_sub.py", 'wt')
fileout.write(parse)
fileout.close()