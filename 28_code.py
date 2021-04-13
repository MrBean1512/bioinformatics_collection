import random

# open a file to get the input
file = open("28_input.txt", 'r')
lines = []
for line in file:
    lines.append("{}".format(line.strip()))
file.close()

# parse the input into useable variables
pattern = lines[0]
dnaList = []
temp = lines[1].split()
for i in temp:
    dnaList.append(i)
del  temp


def computeHammingDistance(text1, text2):
    #comput the hamming distance between two strings
    index = len(text1)
    count = 0
    for i in range(index):
        if text1[i] != text2[i]:
            count += 1
    return count


def distanceBetweenPatternAndStrings(pattern, dnaList):
    k = len(pattern) # max kmer size
    distance = 0    # distance default
    for dna in dnaList: # for each dna string
        hammingDistance = len(dna) # the maximum hamming distance
        for i in range(0, len(dna) - k + 1):
            kPattern = dna[i:i+k]
            if hammingDistance > computeHammingDistance(pattern, kPattern):
                hammingDistance = computeHammingDistance(pattern, kPattern)
        distance = distance + hammingDistance
    return distance


answer = distanceBetweenPatternAndStrings(pattern, dnaList)
print(answer)
fileout = open('28_sub.txt', 'w')
fileout.write(str(answer))
fileout.close()