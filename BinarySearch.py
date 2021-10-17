def BinarySearch(array, x, low, high):
    while(low <= high):
        mid = low+(high-low)//2

        if(array[mid] == x):
            return mid
        elif(array[mid] < x):
            low = mid+1
        else:
            high = mid-1
    return -1

array = [44,67,78,89,90,123,334,567,889]
x = 334

r = BinarySearch(array, x, 0, len(array)-1)

if(r != -1):
    print("Element is present in the array at index " + str(r))
else:
    print("Element is not present")