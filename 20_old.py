text = "ACGT"
d = 1

def neighbors(pattern, d):
    if d == 0:
        return {pattern}
    if len(pattern) == 1:
        return {"A", "C", "G", "T"}
    neighborhood = set()
    print(pattern)
    suffixNeighbors = neighbors(pattern[1::], d)
    #print(suffixNeighbors)
    for text in suffixNeighbors:
        if hammingDistance(pattern[1::], text) < d:
            for x in pattern:
                neighborhood.add(x + text)
        #else:
        neighborhood.add(pattern[0] + text)
    return neighborhood

def hammingDistance(text1, text2):
    count = 0
    for i in range(0, len(text1)):
        if text1[i] != text2[i]:
            count += 1
    print(text1 + " " + text2 + " " + str(len(text1)) + " " + str(count))
    return count

print(neighbors(text, d))