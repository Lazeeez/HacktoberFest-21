def merge(l,li,arr):
    n=len(l)
    m=len(li)
    i=0
    j=0
    k=0
    while i<n and j<m:
        if l[i]<li[j]:
            arr[k]=l[i]
            i+=1
            k+=1
        else:
            arr[k]=li[j]
            j+=1
            k+=1
    while i<n:
        arr[k]=l[i]
        i+=1
        k+=1
    while j<m:
        arr[k]=li[j]
        j+=1
        k+=1
    return arr
def ms(l):
    if len(l)==0 or len(l)==1:
        return
    m=len(l)//2
    l1=l[:m]
    l2=l[m:]
    ms(l1)
    ms(l2)
    merge(l1,l2,l)
    return l
l=[int(x) for x in input().split(" ")]
print(ms(l))