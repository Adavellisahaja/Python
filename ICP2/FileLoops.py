inFile = open("sampletextfile.txt",'r')
ans = {}
line = inFile.readline()
while line != "":
    # lowercase the whole line so same word can count without case sensitive
    line = line.strip('\n').lower()
    # splitting words using split function with space parameter
    for i in line.split(' '):
        if i in ans.keys():
            ans[i]+=1
        else:
            ans[i]=1
    line = inFile.readline()

for i in ans:
    print (i,':',ans[i])