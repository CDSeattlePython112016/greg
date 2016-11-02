import random

rndList=[]
for count in range(100):
    rndList.append(int(random.random()*10000))
print "Unsorted:", rndList

for i in xrange(len(rndList)-1,0,-1):
    for j in xrange(i):
        if rndList[j] > rndList[j+1]:
            (rndList[j], rndList[j+1]) = (rndList[j+1], rndList[j])

print "Sorted:", rndList
print rndList == sorted(rndList)
