#print sum of 3 min elements in list for not repeated values
a=list(map(int,input("enter the val").split()))
a.sort()
print(sum(a[:3]))
