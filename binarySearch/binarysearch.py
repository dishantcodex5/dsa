def binarysearch(nums:int ,target:int):
    n=len(nums)
    low=0 
    high=n-1
    
    
    while low<=high:
        mid=(low+high)//2

        if nums[mid]==target:
            return mid 
        elif target>nums[mid]:
            low=mid+1 
        else:
            high=mid-1 
    return -1

if __name__=="__main__":
    a=[1,2,3,43,22]
    target=3
    
    ind=binarysearch(a,target)
    if ind == -1:
        print("the target value is not present in the array ")
    else:
        print("the target value is present at index:",ind)