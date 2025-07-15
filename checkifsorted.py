def issorted(arr,n):
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            return False
    return True

if __name__=="__main__":
    arr=[1,7,4,5]
    n=len(arr)
    ans=issorted(arr,n)
    
    if ans:
        print("true")
    else:
        print("false")
        