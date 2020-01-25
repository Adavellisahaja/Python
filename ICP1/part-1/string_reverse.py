l = list(str(input()))
from random import randint

if len(l)>2:
    del l[randint(0,len(l)-1)]
    del l[randint(0,len(l)-1)]
    #for i in l[::-1]:
     #   a.append(i)
    a=l[::-1]
    print("".join(a))
else:
    print ("give longer input")