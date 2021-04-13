import random

# open a file to get the input
file = open("29_input.txt", 'r')
lines = []
for line in file:
    lines.append("{}".format(line.strip()))
file.close()

# parse the input into useable variables
k = int(lines[0])
dna = lines[1]

def kmerCompostion(k, dna):
    # return a list of all the dna counts
    kList = []
    for i in range(0, len(dna) - k + 1):
        kList.append(dna[i:i+k])
    kList.sort()
    return kList

answer = kmerCompostion(k, dna)
print(answer)
fileout = open('29_sub.txt', 'w')
for i in answer:
    fileout.write(i + "\n")
fileout.close()