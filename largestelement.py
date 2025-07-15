def findlargestelement(arr,n):
    max=arr[0]
    for i in range(0,n):
        if max<arr[i]:
            max=arr[i]
    return max

if __name__=="__main__":
    arr1=[1,2,421,112,22]
    n=len(arr1)
    max=findlargestelement(arr1,n)
    print("the largest element of the array is :",max)