comp = { "A":"T", "G":"C", "C":"G", "T":"A" }

def ReversedComplement(d):
    return "".join( [ comp[x] for x in reversed(d) ] )

########################################
# Read file input and generate a result
########################################

filein = open("rosalind_ba1c.txt")

#read file and strip new lines and whitespace
instring = filein.read().rstrip()
outstring = ReversedComplement(instring)

# write the file to upload
fileout = open("9_sub.txt", 'wt')
fileout.write(outstring)
fileout.close()