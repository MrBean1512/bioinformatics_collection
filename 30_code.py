# open a file to get the input
file = open("30_input.txt", 'r')
lines = []
for line in file:
    lines.append("{}".format(line.strip()))
file.close()

def combineKmers(kList):
    dna = lines[0][:-1]
    for kmer in kList:
        dna += kmer[-1]
    return dna

answer = combineKmers(lines)
print(answer)
fileout = open('30_sub.txt', 'w')
fileout.write(answer)
fileout.close()