import itertools

file = open("22_input.txt", 'r')
lines = []
for line in file:
    lines.append("{}".format(line.strip()))
file.close()

k = int(lines[0])
dnaList = lines[1::]

def sharedMotifs(dnaList, k):

    # make lists of all kmeres
    parentList = []
    for line in dnaList:
        kList = []
        for i in range(0, len(line) - k + 1):
            if line[i:i+k] not in kList:
                kList.append(line[i:i+k])
        parentList.append(kList)
    
    # count the number of occurances of each kmere
    motifs = {}
    for line in parentList:
        count = 0
        for kmere in line:
            if kmere in motifs:
                motifs[kmere] += 1
            else:
                motifs[kmere] = 1

    # get the most frequent motifs
    frequentMotifs = []
    maxValue = 0
    for key, value in motifs.items():
        if value == maxValue:
            frequentMotifs.append(key)
        if value > maxValue:
            maxValue = value
            frequentMotifs = []
            frequentMotifs.append(key)
    
    return frequentMotifs

# parse and print the most frequent kmeres
solution = sharedMotifs(dnaList, k)[0]
print(solution)
fileout = open("22_sub.py", 'wt')
fileout.write(solution)
fileout.close()