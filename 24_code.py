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


baseIndex = {'A': 0, 'C':1, 'G':2, 'T':3}

def greedyMotifSearch(dnaList, k, t):
    # performs the greedy motif search algorithm
    bestScore = len(dnaList[0])*t
    bestMotifs = [dna[0:k] for dna in dnaList]
    
    for i in range(len(dnaList[0]) - k + 1):
        kmer = dnaList[0][i:i+k]
        motifList = [kmer]
        for j in range(1, t):
            profile = formProfile(motifList)
            motifList.append(mostProbableMotif(dnaList[j], k, profile))
        score = scoreMotifList(motifList)
        if score < bestScore:
            bestMotifs = motifList
            bestScore = score
        print(motifList)
    print("  ",bestMotifs)
    return(bestMotifs)

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
    print("motifs: ", motifs, " \ncolumns: ", columns, " \nmaxcount: ", maxCount, " \nscore: ", (len(motifs[0])*len(motifs) - maxCount))
    return len(motifs[0])*len(motifs) - maxCount

def mostProbableMotif(dna, k , profile):
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

#print(greedyMotifSearch(dnaList, k, t))
fileout = open('24_sub.txt', 'w')
for i in greedyMotifSearch(dnaList, k, t):
    fileout.write(i+'\n')
fileout.close()