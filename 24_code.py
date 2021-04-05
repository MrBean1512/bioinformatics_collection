# open a file to get the input
file = open("24_input.txt", 'r')
lines = []
for line in file:
    lines.append("{}".format(line.strip()))
file.close()

# parse the input into useable variables
k = int(lines[0].split()[0])
t = int(lines[0].split()[1])
dnaList = []
for i in range(1, len(lines)):
    dnaList.append(lines[i])
del lines

def greedyMotifSearch(dnaList, k, t):
    bestMotifs = []
    for i in dnaList:
        bestMotifs.append(i[0:k])
    for i in range(len(dnaList[0]) - k + 1):
        kmer = dnaList[0][i:i+k]
        nextMotifs = [kmer]
        for i in range(1, t):
            profile = genMatrix(nextMotifs)