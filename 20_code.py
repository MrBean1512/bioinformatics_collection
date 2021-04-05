import itertools

text = "CTAAGTAAG"
d = 2

def genDNeighbors(text, d):
    # example: 
    # text = ACTG & d = 2
        # allCombos at AA
            # __TG  if indexes (0,1) -> AATG
            # _C_G  if indexes (0,2) -> ACAG
            # _CT_  if indexes (0,3) -> ACTA
            # A__G  if indexes (1,2) -> AAAG
            # A_T_  if indexes (1,3) -> AATA
            # AC__  if indexes (2,3) -> ACAA

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

    neighborhood.remove(text)
    neighborhood.append(text)

    return(neighborhood)

neighborhood = genDNeighbors(text, d)

print(neighborhood)

fileout = open('20_sub.txt', 'w')
for i in neighborhood:
    fileout.write(i+'\n')
fileout.close()