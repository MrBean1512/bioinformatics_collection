import itertools
# 2 1 0 0 0 0 2 2 1 2 1 0 0 1 1 0
# initialize variables
text = "ACATCATGTCAGGGACGGGTCGCAGCAGACTTAGTTAAGTTGATGGCCAATGTTGTTCCCTTGATACACTCTTCTGGGAATCGTTAAGTCCAGCTGGCTCGAAACTCTATGGGCGATCTGGTTGAGTTGAATATTAGGCGTCAACGTATTGATTATCTCTCTATATTTTGTACTTTCAGGTCCAGTACATAATTCCTATATAATCTATGGTCCAGCTCGTTCTCTGGCCGTGAGACCTGGGGATGCTCTCCAGTTGTGCTGTGACGCCGAAGCCCAGAGTTCGCTTGCTTCCAGGAGTTATGCTTAGCACAAAATCTCGGTCGGGGCATAAACCCGCGAAAAGTTTTGTGATCCAGACGTTCGGTGTGGCTGCATTCAACGGGTACAGGAGGAGCGAGCCAGTCCGCCCCGACGACGAAGAAGGTAAGAGGCGACTGCTCGCCAGATATACACACATCGACCCGCCGGGGCGTAGCTATCCGACGTCGAACACCGCAATGCAAAACCATGCCTTTATCTATGCGATCTGTATGTTACACGATCGTACGAAACATACCAATAGCTTCTATACACTTCGGTTTCGCTGTCTTTGTCGCCTCTAAATGCAGTAGAGCCCCGCTATATCTCTAGTCGTTAAGGAATAATAGCTCTCGAGCACGAATTGGAGATTGACTCCACTCCTATGCATCGTTCTGGAAATCTACGCCCTTGTAGTCCCCACTAATCATTGATGGCATAGGATAGTGTCGCGAGGACGAGTGTCGTTCTGTTCGTTGCGCT"
k = 5

# make a list of all possible kmeres
allKmeres = [ ''.join(l) for l in itertools.product("ACGT", repeat = k) ]

# turn the list into a dictionary
# (I'm not sure how to do that in the fuction above)
kmereCounts = {}
for i in allKmeres:
    kmereCounts[i] = 0

# count the number of times that each kmere occurs in the sequence
for i in range(0, (len(text) - k + 1)):
    if text[i:i+k] in kmereCounts:
        kmereCounts[text[i:i+k]] += 1
    else:
        kmereCounts[text[i:i+k]] = 1

# parse and print the most frequent kmeres
parse = " ".join(str(x) for x in kmereCounts.values())
print(parse)
fileout = open("17_sub.txt", 'wt')
fileout.write(parse)
fileout.close()