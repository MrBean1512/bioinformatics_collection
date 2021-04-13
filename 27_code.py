import random

# open a file to get the input
file = open("27_input.txt", 'r')
lines = []
for line in file:
    lines.append("{}".format(line.strip()))
file.close()

# parse the input into useable variables
k = int(lines[0].split()[0])
t = int(lines[0].split()[1])
n = int(lines[0].split()[2])
dnaList = []
for i in range(1, len(lines)):
    dnaList.append(lines[i])
del lines


def gibbsSampler(dnaList, k, t, n):
    motifs = []
    for dna in dnaList:
        #randomly select kmers from dna
        i = random.randint(0, len(dna) - k)
        motifs.append(dna[i:i + k - 1])    
    bestMotifs = motifs
    bestScore = len(dnaList[0])*t
    for j in range(0, n):
        i = random.randint(0, t - 1)
        profile = formProfile(motifs[:i] + motifs[i:])
        motifs[i] = profileMostProbableKmer(dnaList[i], k, profile)
        score = scoreMotifList(motifs)
        if score < bestScore:
            bestMotifs = motifs
            bestScore = score
    return bestMotifs

def formProfile(motifList):
    # create a profile matrix
    matrix = {'A':[], 'C':[], 'G':[], 'T':[]}

    for i in matrix:
        for j in range(k):
            matrix[i].append(0)

    for kmer in motifList:
        for i in range(len(kmer)):
            for key in matrix:
                if kmer[i] == key:
                    matrix[key][i] += (1/(len(motifList)))
                else:
                    matrix[key][i] += (0.0)
    return(matrix)

def scoreMotif(motif, profile):
    # score the given motif based on the profile
    score = 1.0
    for i, bp in enumerate(motif):
        score *= profile[bp][i]
    
    return score

def scoreMotifList(motifs):
    #Returns the score of the given list of motifs.
    #could not get my list to score properly but I found some help online here:
    #https://github.com/crazyman9870/418-Bioinformatics/blob/master/HW4/greedymotifsearch.py
    columns = [''.join(seq) for seq in zip(*motifs)]
    maxCount = sum([max([c.count(nucleotide) for nucleotide in 'ACGT']) for c in columns])
    #print("motifs: ", motifs, " \ncolumns: ", columns, " \nmaxcount: ", maxCount, " \nscore: ", (len(motifs[0])*len(motifs) - maxCount))
    return len(motifs[0])*len(motifs) - maxCount

def profileMostProbableKmer(dna, k , profile):
    # determines which motif is the most probable given a profile matrix
    bestScore = -1.0
    topMotifs = []
    for i in range(len(dna) - k + 1):
        kmer = dna[i:i+k]
        score = scoreMotif(kmer, profile)
        if (score > bestScore):
            topMotifs.append(kmer)
            bestScore = score
            bestMotif = kmer
    return bestMotif

answer = gibbsSampler(dnaList, k, t, n)
print(answer)
fileout = open('27_sub.txt', 'w')
for i in answer:
    fileout.write(i+'\n')
fileout.close()