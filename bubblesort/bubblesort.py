import random

rndList=[]
for count in range(100):
    rndList.append(int(round(random.random()*10000)))
print "Unsorted:", rndList
idx=0
sortEnd=len(rndList)
while idx < sortEnd:
    if idx == sortEnd-1:
        idx=0
        sortEnd = sortEnd - 1
    else:
        if rndList[idx] > rndList[idx+1]:
            (rndList[idx], rndList[idx+1]) = (rndList[idx+1], rndList[idx])
        idx+=1
print "Sorted:", rndList
