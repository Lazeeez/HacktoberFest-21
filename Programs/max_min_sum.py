# Max & Min finder (Input in One line List)
# Python Program which take Input of list in single line & give there Max & Min Value

lst = []

for i in map(int,input().split()):
    lst.append(i)

P=max(lst)
Q=min(lst)

print("Max No in List is : ",P)
print("Min No in List is : ",Q)
print("Max+Min: ",P+Q)