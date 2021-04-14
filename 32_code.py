# open a file to get the input
file = open("32_input.txt", 'r')
lines = []
for line in file:
    lines.append("{}".format(line.strip()))
file.close()

k = int(lines[0])
dna = lines[1]

def deBruijnGraph(k, dna):
    #this is the main function
    kDict = {}
    for i in range(0, len(dna) - k + 1):
        print(dna[i:i+k-1])
        if dna[i:i+k-1] not in kDict:
            kDict[dna[i:i+k-1]] = [dna[i+1:i+k]]
        else:
            kDict[dna[i:i+k-1]].append(dna[i+1:i+k])    
    return kDict

def parse(kDict):
    parse = []
    for key, value in kDict.items():
        parsedList = ",".join(str(x) for x in value)
        parse.append(key + " -> " + parsedList)
    parse.sort()
    return parse

answer = parse(deBruijnGraph(k, dna))
print(answer)
fileout = open('32_sub.txt', 'w')
for i in answer:
    fileout.write(i + "\n")
fileout.close()