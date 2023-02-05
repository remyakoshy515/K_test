f1 = []
import fileinput
for line in fileinput.input():

#with open("variant.tsv") as f:

    #for line in f:

        list = line.split('\t')


        f1.append(list)

        col = len(f1[0])
       # print(col)
lastcol = []
for i in range(len(f1)):
    lastcol += [ f1[i][col-1] ]
#print(lastcol)

del lastcol[0]


lastcol.sort()
printlastcol = '\n'.join(lastcol)
print(printlastcol)


