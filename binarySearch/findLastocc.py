def findLastOcc(arr,x,n):
    low=0 
    high=n-1 
    ans=-1 
    while low<=high:
        mid=(low+high)//2 
        
        if arr[mid]==x:
            ans =mid
            low=mid+1 
        elif arr[mid]>x:
            high=mid- 1
        
        else:
            low=mid+1 
    return ans 

arr=[1,2,12,12,12,3,12,7]
n=len(arr)
x=12
finalans=findLastOcc(arr,x,n)
print("the final answer is :",finalans)