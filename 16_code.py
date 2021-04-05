import itertools

dnaStrands = []
dnaStrands.append("ACACGTGCGAGAACGCTAAACCGGGTGGAGAACGCTACACGTGCGAGAACGCTATACTCAGAAACCGGGTGAAACCGGGTGATACTCAGCGCGACAAAGATACTCAGACACGTGCGAGAACGCTATACTCAGATACTCAGAAACCGGGTGATACTCAGATACTCAGGAGAACGCTAAACCGGGTGGAGAACGCTATACTCAGGAGAACGCTGAGAACGCTACACGTGCGAGAACGCTCGCGACAAAGACACGTGCAAACCGGGTGACACGTGCACACGTGCACACGTGCATACTCAGGAGAACGCTGAGAACGCTACACGTGCAAACCGGGTGAAACCGGGTGAAACCGGGTGCGCGACAAAGATACTCAGATACTCAGATACTCAGATACTCAGGAGAACGCTAAACCGGGTGAAACCGGGTGACACGTGCATACTCAGATACTCAGACACGTGCGAGAACGCTACACGTGCGAGAACGCTCGCGACAAAGATACTCAGCGCGACAAAGGAGAACGCTAAACCGGGTGCGCGACAAAGATACTCAGGAGAACGCTGAGAACGCTGAGAACGCTCGCGACAAAGGAGAACGCTACACGTGCAAACCGGGTGACACGTGCCGCGACAAAGGAGAACGCTATACTCAGAAACCGGGTGATACTCAGACACGTGCAAACCGGGTGAAACCGGGTGCGCGACAAAGAAACCGGGTGACACGTGCCGCGACAAAGACACGTGCGAGAACGCTAAACCGGGTGACACGTGCACACGTGCCGCGACAAAGAAACCGGGTGGAGAACGCTGAGAACGCTATACTCAGAAACCGGGTGCGCGACAAAGGAGAACGCTGAGAACGCTAAACCGGGTGAAACCGGGTGATACTCAGAAACCGGGTGATACTCAGGAGAACGCTATACTCAGATACTCAG")
k = 5
d = 3

# create the reverse compliment
# this is not just appended to the first string because the 'codons' would mix
dnaStrands.append(dnaStrands[0][::-1])
compliments = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
text = ""
for i in dnaStrands[1]:
    text += compliments[i]
dnaStrands[1] = text


allKmeres = [ ''.join(l) for l in itertools.product("ACTG", repeat = k) ]
kmereCounts = {}
count = 0
for strand in dnaStrands:
    for allK in allKmeres:
        #loop through the list all possible kmere combinations
        for window in range(0, len(strand) - k + 1):
            #loop through the nucleotides in the string
            count = 0
            for i in range(0 , k):
                #loop through the current nucleotide window/kmere
                if strand[window+i] != allK[i]:
                    count += 1
                if count > d:
                    break
            if count <= d:
                #if the characters are the same with less than d mismatches
                #then add the string to the dictionary
                if allK in kmereCounts:
                    kmereCounts[allK] += 1
                else:
                    kmereCounts[allK] = 1

max = 0
largestK = []
for key, value in kmereCounts.items():
    # make a list of all of the most frequent kmeres
    if value > max:
        max = value
        largestK.clear()
    if value == max:
        largestK.append(key)

# parse and print the most frequent kmeres
parse = " ".join(str(x) for x in largestK)
print(parse) 