
# map out all of the patterns (that are the size of the kLength or k variable) and the index of where each pattern is occurs
def map_k_mers():
    for i in range(0, (len(text) - kLength + 1)):
        if text[i:i+kLength] in count:
            count[text[i:i+kLength]].append(i)
        else:
            count[text[i:i+kLength]] = [i]
    #print(count)

# remove all of the key values from the dictionary that occur under kCount or t times
def cull_map():
    dict_removal_queue = []
    for key,value in count.items():
        if (len(value) <= kCount-1):
            dict_removal_queue.append(key)
    for i in dict_removal_queue:
        count.pop(i)
    #print(count)

# get all of the clumps from the dictionary values
def get_clumps():
    clump_list = []
    for key,value in count.items():
    # iterate through the count dictionary
        for i in range(0,(len(value)-kCount+1)):
        # iterate through the values in each dictionary
        # the iteration takes place (len(value)-kCount+1)) times to iterate as a window
        # the window considers if there is a clump that takes place after the first valid key
            if ((value[i+kCount-1] - value[i] + kLength -1) <= clumpLength):
            # checks if the values in the window are a valid size clump. In the example this would be 75 or L
                clump_list.append(key)
                break
    parse = " ".join(str(x) for x in clump_list)
    print(parse)

text = "CTCGAACCACACGAACTAGAAGATACAATGCTTATGCGATCATTAGTGCATGTTGTGGTCTTCCCCGCAAATCTCATGTACCCTTCTCGTGCGTATGTGTTTGATGCTCATGCCATCGGGACTAAGACAACCATAGACCGAGAATGACTTCAATGTACGGATTGTTACATCTAATTCAGCGGCGGGTTCCCTACTGGAGGGGCAGTCTTTGTTGGCCGTTCGGCACATTTTTACTGGGGCTCCATTGGGGGACTTAAGCAGTAGTCTCGTAGTACACCCTGTGAAACCAAACCTTCGGGACATGGAATGAGAAATCTACGAGAGGTCTAGGCCTCTAGTGATGTCGGACGGCAGAACAAGGCCTCTAGTCCAACGTGAGGCCTCTAGTATACGGAATTTGTCGGACGGACGGGCCTCTAGTGTCGGACGGCCTCTAGTACAGGCCTCTGGCCTCTAGTTGTCGGACGGGTGGCCTCTAGTTAGTGGGTGATGGCCTCTGGCCTGGCCTCTAGTGCGTCTGGGTGAACATTCTCGTTTAGGCCTCTAGTTGTCGGATGTCGGACGGAACTGGCCTCTAGTATTGTCGGACGGGGTCGTCTGCTGGCCTCTAGTTTATGTCGGGCCTCTAGTGACGGGATAATGTCGGCCTCTAGTTGGGCCTCTAGTGACGGTTGATTACGGCGGCCTCTAGTTGAGGCCTCTAGTCCTCTAGTGCTTGTGTATTGATTAGGGCCTCTAGTGGACGGAGGCCTCTAGTCTGTTGATTACTGGCCTCTAGTCTGGCCTCTAGTCCTCTAGGGCCTCTAGTTACTGGTGGGCCTCGGCCTCTAGTTTGTCGTGGGCCTCGGCCTCTAGTCTGCGGTTGATTACTGACGGGCCTCTAGTGATTACGGCCTCTAGTTTACTGCTATCGCAGAATTTGATTACTGACTGCACACTGCTCATTCCTACGTGTTGCCGGCTGCCACGGTTACATCGTCCCTTGATTATTGATTTTGATTACTGAATGAAGTAGTTGATTACTGTTGATTACTGATTAAACTTCACCGAGTCGGTGGACCGTTATTGATTACTGAATCCATGAAACGACTTGATTACTGAGGACTACTTGTCCAGGTCTTGATTACTGACAACTACAATGATACACATGCTGTCCCAGTCATCATTGCCTTGATTACTGTACTTGATTACTGTATTTTATCTCGGAGTGCTTGTATAGCTTGATTACTGAACCTCTGAGCGTGAAGCCACGCACAGATATGGATTATGCGGCAGCCCATCCGAACCTCCAGTTGACATGCTGTTCAAACGTGTGGTCCTTACGAAAACACGAAAAATCTTATGCACGTTGTATAGTGCATGAGCTGAGGTAATTGACAATGAAGCAAAGGCATATGAGTCAAGGAGTCACCTCACCACCTTTGAGTCGTCCCGCGACCAATGTTTCTTACCTTTGGCCGCCTCGGACCATAGCACCCGTCTGGAGCGGTCCGTGTGCATCCTGGCGCATTACGAATCTATATGCGGTGGCAGTCTTTACGTTGAAGCGGTGCTCATCATTTCGTTGTCATGGTACGCCCAGGTGCTCAAGTTATGACTGAGCGACGCTCTGGTCACAAAAAAATAGCGAGAGTCGGCAGGCACCTCCGTGTAACGCAAGAGATGGGTAAAATCATAGAATTCAAGGTCGCGTTACGCGGGCACAGGTGCACTACTAATCTCTAACAAGCTTTGAGGCACCCCGTAGCTCACTCCACTAAAAGAGCGACTTAGTTCTGATTGACGAGTCCTATACGCAACATCCTACTGCCTCGGAGGATATCCTAAAGCGATTCCTGTGTACAAACCGCGAATACGGAATTTCTTCAGCCCGCTAGGTTGTCAGTAAGCTCCTGTATTTATTAAAAGCCGAGATAGGCAGGGGGAAGATCAGAATCGACCCTATCTTTTAATTAAAAAGACGTTCTCAAAGATAATCATACGGTGAGTCATGATGAGTACGAGTAGCCTTGTGGTCCCACATGACTGTAAATCATCGGAAACGAGCTAGCCATGTCCAAGTGGCAGCGGACCCTGGTTTTTAGTAATACCAGTGAGGGTACGTACACCACACCGTGCAGTCTGGCTGCAAAACACTATCATCGACCCGAACGAGGCCACACGATCGCTCAACAACACGATCGCTCACGATCGCTCGCTCGATCGCCACGATCGCTGCGTTAGCAGCTTTCTTTACTCCAAGTTGCGCAGCGTGCTATAGCCCGCGGCAGCCCGCACACGATCGCTTCGCTCACGATCGCTGCTGCATGAAGGCTCCTATACTGAGTTCTTGACGCGGGAACGGAGGCGTACCACGATCGCTTATGGAACTCGCACGATCGCTACAAGGGTTATTACACGATCGCCACGACACGATCGCTTGCTAAGCACCACGATCCACGATCGCTGCTGTCGCATCTTGGCCTCCACGATCGCTCTATATTATTGCGAATCACAGGGTGCTGCGCCGACAGATATCAAATGGCTTGCAGCGGACCACGATCGCTTCCCCGGGCATTACTACTTTTCATCATTTCACGATCGCCACGATCGCTGCTTGCACACGACTGACCTTGCACCACGATCACGATCGCTGATCGCTCACTTAGAGACTTAAGAGGTCCACGATCGCTCGCTCCGCTAGAAATGGAACGCAGCACGATCGCTGCGTACCAGCTCACGATCGCTCACGATCGCTGGAGCTACTCACGATCGCTCCGTATCATTTTATTATTCTACACTTGTCCTAACTAAACTACAAACGGCGTACGACGTCATTTGGAACTACAAACCTGGAGTGGTGCCTAAACTACAAACAACTACAAACAAAAACTACAAACGGTGATTCATTCGGGGCGGCTTACGCCAATCACCTGAACTAAACTACAAACCCTAACTACAAACACGATATAACTAACTACAAACAGGCGCCAGAATATTCTCGAACTACAAACACAACTACAAACAGACATTGATCGCGCCTTATACTTAGTCTCATCCCAAACTACAAACAAACAACTACAAACACGCCTAGTGAGGCTGTCATTACATTAGTAGATGATAACAGCTGAACCCTCGGAAACAACTACAAACAAGCTAGGCAGTACTGAGGAAAAAGGGTAAGACAAAGCCAACTACAAACGTTGACGCCGACACAACTACAAACATGAACTACAAACTACACTGGAACTACAAACAACTACAAAAACTACAAACGACCTAAACTACAAACCCAATGCCAATGTGTTTGAAACTACAACTACAAACTGGGAAATGAGGCCACAAAACTACAAACATGTGTTAAGTCAACTACAAACACAACTACAAACGATCTCTTCTAGGAGTTTCACGCGCTCAAATTGCACTGCCGATGGGCCAATGTGTTCCAATGTGTTAGTATACCGTCTCCAATGTGTTGTTTACATGAAATTATCCCAATGTGTTTGGCTAAGTAACGTCTTGCACTTGTCCAATGTGTTCTCACTTGAGTAGTCAGAATGACGCCAATGTGTTTTCGGGGTTGCCGCCAATGTGTTCCCAATGTGTTACCAATGTGTTCACCCAATGTGTTTACTCCAAACCCAATGTGTTGTTTGAGAACTGGCTAATTCCAATGTGTTATCTTGGCCAATGTGTTGTGTTACGTGCCAGCCAACGTGCCTTCTTACGGGTTCCAATGTGTTCCCAATCCAATGTGTTCCAATGTGTTTTATCCGCCCAATGTGTTGAAGAACAAGCCCTTCTTCGTTTTGGGAGGAGCCAATGTGTTGTGTTCAACCAATGTGTTACCATCCCAATGTGTTGTCCAATGCCAATGTGTTTGGGGCTGTTGGAGACGTAGACCTACCATCGTTCACTCACGATAAGCGCGCGCGTCGGTCTGAAACGAGTATAGCAAGACGGTCTGCTCGCGCGCGTCCGAAGAGTCAATGTTATACACGACAAGTATTGGCCCACGCATACAGACGGGAGGCTAGATGGTGTCCTCACCGGTGGCAGCAGGCGCACGCTCAGCCCGTGATATCTCGTTAAGACGACCAAATAGGGAACTCCCAATTGCAAGAGGTCAAGGATCTGAGTCCTAATTAGGCTAGAGAAATGATTTTGCCTCTTACTCCTGGTTTTACACACGGCCGAGAGGCTATCTTCACTTTCGCTTTAGAGAGGCTAGTCCCGGAAGGAGTGCGCGTAACCGCATGAATGCGCCCGTTCAAGGTAGTCTTGGCGGAGGCTGAGCGTTCTACGAAATACATATAGTACGCTCACAAGCCGGTGTACTACATGGTTCCTAGACAATATAATGGAATTAGCCTAAGATTCCGCTAGTTCGATTGGCCCGTATAATGTTGACGATCATTTTACCATCCGCTTTTAGAGCTTGTAGCCGTGCAACTAGAGAATGTGGCATTAGAAGTCAAACTGCGCTCGGACAACACTAATGCCAACGTCTGATGAACAAAAGCCCTGCAGCCCTACTCGGGACCGAGCATTACCTCATATCAATGTTATCCTAAAGCACTACCCCCGTTACCATCATCGCGTCGGCCGACTGGGAAACATCCCCCTTTGTGCAAGTTATATCAGGCGCTTCTGATTAGAAAAGTATCACTCTACGTCTTGGTTGAATCTTTCTGTCGGGTGAGATTGTAAGGAGCTAGCCGGCCCATGGATGGGATCTGGAGTTGGTTAATGACAGGGACAGGAACCGTATCGCAACTCGCATTTCATTAGCGACAAAGAGGACTATGTTCCTGTTCTTGGAATTGGAAATATATTCTCGGTTGCATCTCCGAACACGGCCCATATTTGATTTTCTGTCAATGATTCGAATACTACCCTCCCCCGAATGATAATTATCCCCGGACAACCGAGCTCGTCGTGACGATCGCGAAGAATTAAACTTTCCGGCATCTCAAACAGCACGGATGTTGCCCCTGTGGATTTAGGCATCATTTTGACTTACGACATAGAACCAAGACGGGTCACTGCAAAAAACGATAATGACCGGTTGGTCCGACCCGCCTTTCGCTGGCTAGGGGCGTATTCTAAATAAACCTATCTATCATCCTCTCCTCAGCAGAAGGTACGGCTCCAGGTGGTACGACCTACTAAGAGACTCACTATCATATGTACTGACCCAGTGTCCATATGTTACAGGGCTCCATAATACACCTAAACTTAGGCCGCGCAAATGCTCAGAGCTAGTTCCGTGCCCCATATAAGGATCTTCTAGGGTCTTCTTTACTCGCACTACTCCCGTAAGTTTTGTGTGTCACATACCGCTTCCTAGTCCATTACTTACTATTGTAGCATCGCTCGACCGAAGGCCACATTGCCGACTGCTAAGTCGCAACCCAAATCTGAGCGCCCTCGCAGCTCGTGACGTACCTTCTTGTTCAACTCGGCCAGGTAATATCTCTACATCATACAATCATCCGCACTCACGTAGTATTTAATCAGCGGCGGCTTCCAAGCCGTCAAAACGGATCACGCATCACCTAATACGGATATATTCTGCCCGTAATTGGGCCTGTCGGCTTTACTCAGGGCCCGAGTTCACTTAAGCAGTGGAGTGGCTGTGTCGCTCTGTTGTAGAATTAATTCACATGCGTTGGGTCGATAGGATAGCTGTACAGCTGACGTACGGAACTATTGAAGACCTGTAATTATAGAAGGACGCCGCCATAGCTTACGACGCAATCACCTAATCCTTAGCAAAGGACTGTGTAATAGTATGTAGCGATTCAGCGCCTGCGCTCCCGGGAATGCTAATCCATCCCGCTCTTAATGGGGGAGGTCTGAGACGACCCTTTCTCGATTCTAACAAACCGTTAGGCCCCGCTGTTACAAATGGCAAACCATTTCCGTGAGCTCGCCCCGTCGTAGACCCCATATACAATCCTATATTCACTATCACATCGACTGAACATCCACGTTAACAGACGATGGTAAATGAGATTTTCATCTGGGCTTCTTACCACTGATTACCCGGTGACGACTTCGGTCGCACTCCGGGAATGACATCGTCTTTACGGCCCTTTGAGGGAGGTCCAAGGATGAGCATTCTGATAATACGATGATCTTAAAGCACGATCGGAAAAACCCTTGTTTATCTTAAAGTGCTGCCTGGCGGAATAGTGTCTATCCTATCTGCATTCCCACACTTCCAAAGCTTCGTCCAGGGCAGGCTGTGAAGATTGGTCAGACAGCAGCACGTAAGTCAACATCTGGTCGGCCACGGAAACTGCCCTGGATCGATTGGCCTGCGAACAGATTTACTCGGTCGCCATTCGTGAACCCTGTGTACGAACGAGGGAGCACATTACCCGGGCCGCGATTTTCCGACGATCTACTCAATCCGCCGGCTGAGCTTCCCTATTACCCGTACCCGCCCAGCAGATTCCTAAGAAACAGAGTTTATAACAACAGGCCGCTACATGGCTTACCGGTAGCCAGCGGGGAATTCCTGTAAAAAGTTGCGCATTTTGACTGTAGGGATCTTCTGTCCTCGTACTCTCTGAACGGATTCCGAGAGCAGTCTGGATCTATTAGTAGATACACTACTTCGGCGGTGCACTTAGATACACTAGATACTAGATACACTTAGGTAGATACACTTAGATACACTAGATACACTATAGATACACTACTGGGGAGATGGTAGATACACTTCTAGATGCTTTTAGATACACTTCTCCGTGTTAGATACACTAAAAGGCTCGTTCGAAGGATACCCGGGACTGGGTATGCAATGCGGTCCTAGATACATAGATACACTATGTACAAATGCTCAGCAGTAGATACACTATACACTCCTATAGATACACTATACTAGATACACTAGATACACTCCTAGATACACTCCCGTACTAGGTAGATAGATACACTACACCGGACGTAGATACACTAGTCATCAGATAAAGTCTCTTACGTCTCTAATCGCCCATAGATAGATACACTTATCTGTAGATACACTAGAGCTGTCCGCTAGATACACTCAAATGTTAGATACACTGATATCTACCTAGCAAACGTTTATCACGTAATTTGTATAACGGTCATCTCGGTAGATACACTGTTAAGGGACCACAGAGCGTTCTAGTAGATACACTACACTTGTCGACGACAAATACGTATGTGCCGCACTTACGGCCCGCCTGCAGAGTCATGTTCGGTAAAAGGTACAATTAAAGTAAAATCCAGAAAAAACCCTACTTGTCGGTACGAGCAGGCAACGGTAGCACGGGGACATGTACCCCAGCGCGAGACCCCAGGTTCTACTTTACCATCTTCGGGCACTGACTGGGAATCGCCTAGCACCTATGTTTCAACTATTTGGTCGTGAGTAAGTCGAATCTAAGAGGTTACGAAGGTGCTATACCTCTGTCCAACACGTTTTTACCCTTCAGCTGGGCCACGAGGGTCATAAAGGAAATACGGGTCGGCTTTTAACAACGAGTGAGGTATAACGCTCCGCGCTAGATCCAAATTATAGATCCAAATTAGATCCAAATTAGAAGGCGGATCCAAATTAAACCGTTACGAGCTACAGCTTTGTGTTACACCTGCACCGGCCGATCCAAATTAATCCAAATTAATCCAAATTAAAATTAATGATTGAATCCAAATTAATTAAAATCCATCCAAATTAACGCGATAAGGTTATGATGAAGCCAAACCGGGCCGCTAGGAATCCAAATTACTATCGGTAGCTTAGGAGATCCAAATTATGGACACATCCAAATTAGTTAATCCAAATTAAAATTAAGGTCCTAGATCCAAATTACTGCGTAGGAGCTATAGAACATCCAAATTATCCAAATTAAATCCAAATTATGTGATGTCCGATCACAGAATCCAAATCCAAATTACAAATTATCCAAATTAAATCCAAATTAATCCAAATTAAATTATTCATCCAAATTAATTACACACAGATTTACACAGATATCCAAATTATCTTTCGACTGGATGAGTATCTCGACACAGATTCACAGATTTATCCAAATTACAAATTAAATCAAGTGTACACAGATTTATTTATAGTCACAGATTTACAGATTTACTCACAGATTTAACACAGATTTATTAGATTTATTCCAGCTATCACCGAAGCAAATGGTATACCACACAGATTTAACACAGATTTAACAGATTTACACAGATTTACCACAGATTTATCTTCACCTTCTGGTAAAGGAGAGCAGACCCCAGTATTTGGAGCGTTATCGTTAAGTTAGGGTCTGCGGTCCACTCTGCATGTAAAGCGACACAGATTTACACAGATTTAAGTCTTATAGGCGACACACCACAGATCACAGATTTAGTTTTAACGGATACTATTTCCATCACAGATTTATCCGTCGTTAAAGAAACGACGAAAGAAACGACTAAGAAACGACAGAGGGGGAGCCAGCGCGTGTGAATGCAAGAAACGACACTTGCGAAATACTGACCCGCCCCTAGGAACTAAGAAACGACAACGACGGCTACTAACCACCTCAAAGAAACGACTTAGTCTCTGCGGATGCGACAGGTAAATAAGAAACGACACGAAGAAACGACCTAACGTAACTGACCACCAAGAAACGAAGAAACGACCATGATAAGAAACGACAACGACAAACGACAGTGGCCAAGAAGAAACGACGGAAGAAACGAAGAAACGACTGGCAAGTTGTGCCATAATACATTAGGATGCCATAAAACGGGAATATATACGCGATGTCTGCGTCTGGCAGATCCAAGAAACGACAGAAACGACCCATGGGCGCACACTGGTGTAAGAAACGACGAAACGACACGACATTTGAAAGAAACGACATTCACGACTCACTTCGTCCGGGAAATAAAAAGTAACTCGCCCGCTGAAGAAACAAAAGAAACGACGAAAGAAACGACGGGTTGACCAAAGAAACGACCCCCGCGTCCAAGGTCCGCGACAAGTGATAAAGAAACGACAATAGAAATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTATTCCACGTTCCACGTTATTCCACGTTAATTCCACGTTTTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTTATTCCACGTATTCCACGTTTATTCCACGTTATTCCACGTT"
kLength = 10
clumpLength = 536
kCount = 19
count = {}

map_k_mers()
cull_map()
get_clumps()