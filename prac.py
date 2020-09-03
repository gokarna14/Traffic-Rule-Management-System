from physical.objects import Operation
from operator import itemgetter
vehicles = [12,23,1,4,12,4,213,4,124,21,4,21,321]
temp = []
for i in range(len(vehicles)):
    temp.append((vehicles[i], i))
temp = sorted(temp, key=itemgetter(0,1))
print(temp)
print(temp[0][0])