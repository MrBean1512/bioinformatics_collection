text1 = "ACAAGATGAAGCCAGGCGCTCCCCGATGCGGTGCGGTGGGATCAGGTGTGCGACGGATTTTTCCTGGAACCCGGGTGACTACCGTTCTCGCCCCCATCGCTACTGTTACGTTGCTCCGAAAAGGTACTTTAGGATCGCTTACAGATCGACGTAGTGTAACCGAGCAGGACTCCAAGGGGATGTGCCTGGAAGCACTCAGTTTCGACAGGGTGTATTTCTAGTTTGGTGCTTTACAAACAATTTCAGTCGGGTGCAAAACAGCACTCACCGCGATACCCGCGTACGTTCCTATTATTTATAGCTACTTTGGCTCGTCAACGGAGTGAACACTCGGTGTCGCTCAAGCCAACGACAATGGATATTGCGCTTGGTGCTGCACCACCTGCTTATCTGGGATATCACTGGTCGTTTCGCCCTGGCTGGTTCAGGGATGTACCCTCAAAGCCACCTAACATGCACTCCTTCTCACAAGCAAGGCCTACCTTACGGACATTAGGCGTAAGAGCCCTTCTTACTGGTACTCAGGAATAGGACCTCCCAGTTGTGCGTTACTGTCCTTTGTGATTGTCGCTCCTTTCTCGTAGAAGGCTTGTGGGGAGCCAGCAGGGTCGCTTTACTGGTGTCCCAAGCTCAGGTAACTTCTTCTGCCCATAATGAGTTGGCGCTAGGCCGACGGCCTAGACCTGGATAGACAGCAACGTTTAGCCAGGAGGTCATGGATGTGCAGTTTTTCACAAGCGAAACTCTGTCACGACCACGAAAAGACACGCCCCTAACGCGTATAACGGACCTACAAAGCGCACGTCAAAATGCGTAGGAGAATCAACCGGCATTATGATGTCACGCATAAGTTCGTGGAACGTTCCTCCCCTAGGTCGGAGAACGTGGCGCTAGACCCCACTACAAGGCGCTAACACAAAAGTTAAAATATACTGGTTTTTGGAACCCTATGTATTAGAAAAACTCCTACCAAACTGATGCGGGTGCTTAATTTCCTTCGCTATGTACCACTTTTATAGCAGTGTCGTAGTGGCGAAGAGACTAGCTGAACGTAAGCGGCCTGAAGCCACATTTAGCCAAGCCACGAGCGGAGCCGATTATGCAACACGCCTTAACAGAACAAATAAAGCTGAGATCACGACTCCCGCATCGCACAAATGTCTCACAGCTATCTGTCGGGTCCCGTCCTTAGCTTTC"
text2 = "TAATGTCGATTTCCGCGCCAAGTTATCTAACCAATTGATCTCACTGAGATTCCCAACCGCTAGATACACGCGGACGGGGGGCGGATATGTCCCTGCTGAGATTGGTATCCCAGGTTCTATGTATATAGCAGGGGGCCACACTCCGTGTCCTTGACGACAAAAGTATGTGTGGCCCTATAGCCTCCTTATTTCAAAACAAATCCGGTCATCTTCGAGGCTGATGTCTTTACGTTACGCAAGCCAAGTACACCGATGTAGAGTGGGATTCCCCATCGCATTAGTAATCTCTGTGAACCGAATACAACAGTTTACCCATAGCCTCGCGCCACGAAGGTCACCGGCATACAGAATATTTGAGTGTCCCGTCCCTGAATAGTCGCCACATACCATAGCGGCTGCTCGGGCATGGCGGCTATATTACAGGCGTCACGGATAGCTCTTTCACGGTCGGTTGCCACATGTTTACTTTTTGAAATACATGAGGAGGCAAAGTTCCCTACCACTCGGCCCTTTTTGGCAGTGATGGTTTACCCAATTAGGGCCCTTCAAACCAAACGGCCATTTCTGAGCTGACCTGCCATGTGGTCGCTTGCCTAGTATGTGTTCCTAATACCCATCGGACTTATAGGTCCATGGTGCCTTAGAGCCAAGAGACAGGGGAGGGATATTCAAGTGGAAAGAAGCAAGGTGCTATTGAGAGCAGCGAAACGATATTTTCACTAATCCGGGGGTGCGAGTCGCCTCGTACCTCGAGTAGATGTTTAACTTTTTCCACAAGTGCCGCGAAAAGGCATTAATTGAGTTACTCGTAGAACCAACCGTGAGAGCTTTATAAGGACATAGTGTCGAGTCAGGGGCATTTTTGGGGTTGCAACCGACCAGCCCCGTATCCTCTCATGAATCCTGAGGAACAGTACCGCCCAGGAATGAGGTCAATGACGTAACGTGACTTCCATGCATTTCTCTGCGGGAATGTAAGGAAGTAGTGGAAATCGGCTAGGTGGGTAATTCAAATCTGCAACGTTTCTGTCCGGCAACCGTTCGCGATAGAGCCATTGCTCACAATCTCTCATGATGCTTTCTCCGTTTCGATCCCTACTTTGTGATGATGGTCACACGACGGAGCCCAGCCTCCCTCCGGTCGTTCTTTACCTTTATGTCGTGCTAAGCATATTGATATCATGGGGAATGAAAAGA"

index = len(text1)
count = 0
for i in range(index):
    if text1[i] != text2[i]:
        count += 1

print(count)
