# open a file to get the input
file = open("32_input.txt", 'r')
lines = []
for line in file:
    lines.append("{}".format(line.strip()))
file.close()

k = line[0]
dna = line[1]

def deBruijnGraph(k, dna):
    kDict = {}
    for i in range(0, len(dna) - k):
        if dna[i:i+k-1] not in kDict:
            kDict[dna[i:i+k-1]] = dna[i+1:i+k]
    kDict.sort()
    print(kDict)
    return

answer = deBruijnGraph(k, dna)
print(answer)
fileout = open('32_sub.txt', 'w')
for i in answer:
    fileout.write(i + "\n")
fileout.close()