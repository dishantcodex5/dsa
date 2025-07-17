def remove_duplicate(arr):
    if not arr:
        return 0 
    
    i=0 
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    return i+1 
arr=[1,2,3,3,4,4]
length=remove_duplicate(arr)
print("new length: ",length)
print("array after removing the duplicate:",arr[:length])