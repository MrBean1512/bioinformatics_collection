file = open("23_input.txt", 'r')
lines = []
for line in file:
    lines.append("{}".format(line.strip()))
file.close()


dna = lines[0]
k = int(lines[1])
matrix = []
for i in range(2, len(lines)):
    matrix.append([])
    for j in lines[i].split():
        matrix[i-2].append(float(j))

def scoreMotif(motif, k, profile):
    baseIndex = {'A': 0, 'C':1, 'G':2, 'T':3}
    score = 1.0
    for i, bp in enumerate(motif):
        score *= profile[baseIndex[bp]][i]
    return score

def mostProbableMotif(dna, k , profile):
    bestScore = 0.0
    topMotifs = []
    for i in range(len(dna) - k + 1):
        kmer = dna[i:i+k]
        score = scoreMotif(kmer, k, profile)
        if (score > bestScore):
            topMotifs.append(kmer)
            bestScore = score
            bestMotif = kmer
    return bestMotif


# parse and print
solution = mostProbableMotif(dna, k, matrix)
print(solution)
fileout = open("23_sub.py", 'wt')
fileout.write(solution)
fileout.close()