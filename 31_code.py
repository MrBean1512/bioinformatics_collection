# open a file to get the input
file = open("31_input.txt", 'r')
lines = []
for line in file:
    lines.append("{}".format(line.strip()))
file.close()

def overlapGraph(kList):
    pairs = []
    for prefix in kList:
        for suffix in kList:
            if prefix[1:] == suffix[:-1]:
                pair = (prefix + " -> " + suffix)
                pairs.append(pair)
                break
    pairs.sort()
    return pairs

answer = overlapGraph(lines)
print(answer)
fileout = open('31_sub.txt', 'w')
for i in answer:
    fileout.write(i + "\n")
fileout.close()