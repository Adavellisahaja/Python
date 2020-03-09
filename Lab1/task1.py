#@title Task 1
#Given a collection of integers that might contain duplicates, nums, return all possible subsets. Do not include null subset.

inArr = list(map(int,input('Enter array numbers with space in between: ').split(' ')))

def subsets(arr):
  outList = []
  n = 2**len(arr)
  for i in range(n):
    subset = []
    binaryString = "{0:b}".format(i)
    while (len(binaryString) < len(arr)):
      binaryString = '0' + binaryString
    for b in range(len(binaryString)):
      if (binaryString[b] == '1'):
        subset.append(arr[b])
    if subset != [] and subset not in outList:
      outList.append(subset)
    outList.sort(key=len)
  return outList

print (subsets(inArr))
