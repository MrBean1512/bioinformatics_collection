import itertools

text = "AAAAAAAAAA"
k = 2 # size of k-meres
d = 1 # number of mismatches allowed

# create a list of every combination of chars
allKmeres = [ ''.join(l) for l in itertools.product("ATGC", repeat = k) ]
print("allKmeres done")
        

# add all k-meres to a map with the number of times they occur
kmereCounts = {}
for i in range(0, (len(text) - k + 1)):
    if text[i:i+k] in kmereCounts:
        kmereCounts[text[i:i+k]] += 1
    else:
        kmereCounts[text[i:i+k]] = 1

count = 0
for kmere in allKmeres:
    print(kmere)
    for key, value in kmereCounts.items():
        count = 0
        for letter in range(0, k):
            if kmere[letter] != key[letter]:
                count += 1
            if count > d:
                break
        if count <= d:
            if kmere in kmereCounts:
                value += 1
            else:
                value = 1
        print(value)
#print(kmereCounts)

freqKmeres = []
max = 0
count = 0
for key, value in kmereCounts.items():
    # loop through each kmere
    # this is the kmere that is being checked
    for keyCompare, valueCompare in kmereCounts.items():
        # nested loop through each kmere
        # this is the kmere that the parent loop's kmere is being compared too
        if key == keyCompare:
            continue
        count = 0
        for i in range(0, k):
            #print("    " + key[i])
            # loop through each letter in the nested kmere
            # this checks for single letter differences
            if key[i] != keyCompare[i]:
                count += 1
            if count > d:
                break
        if count <= d:
            value += valueCompare
    if value > max:
        max = value
        freqKmeres.clear()
    if value == max:
        freqKmeres.append(key)
    #print(key + " " + str(value))

parse = " ".join(str(x) for x in freqKmeres)
print(parse) 






ref = {"A", "G", "T", "C"}

def iterativeNeighbors(pattern, d):
    neighborhood = [pattern]
    for j in range(1, len(pattern)):
        for pat in neighborhood:
            neighborhood.append(immediateNeighbors(pat))
    return neighborhood

def immediateNeighbors(pattern):
    neighborhood = [pattern]
    for i in range(1, len(pattern)):
        symbol = pattern[i-1]
        for x in ref:
            if x == symbol:
                continue
            print(pattern + " " + pattern[0:i-1] + " " + x + " " + pattern[i::] + " " + (pattern[0:i-1] + x + pattern[i::]))
            neighbor = (pattern[0:i-1] + x + pattern[i::-1])
            neighborhood.append(neighbor)
    return neighborhood

#print(iterativeNeighbors(text, d))