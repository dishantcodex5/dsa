from typing import List

def upperbound(arr:List[int],n:int,target=int) -> int:
    low=0 
    high =n-1 
    ans =n 
    
    while low<= high :
        mid=(low+high)//2
        
        if arr[mid]> target:
            ans=mid 
            high=mid-1 
        else:
            low=mid+1 
    return ans

if __name__=="__main__":
    arr=[1,2,34,44,55]
    n=len(arr)
    target=33
    ind=upperbound(arr,n,target)
    
    print("the upperbound is at :",ind )
            