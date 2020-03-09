#@title Task 2
dict1 = {'a':21,'b':43,'c':22}
dict2 = {'c':43,'d':2,'e':8}

#this is simple concatenation of dictionary
#last value of same key will be the final
concDict = {**dict1,**dict2}
print (concDict)


#concatenation of dict. by merging values of same key
mergeDict = {**dict1,**dict2}
for key,value in mergeDict.items():
  if key in dict1 and key in dict2:
    mergeDict[key]=[value,dict1[key]]
print (mergeDict)