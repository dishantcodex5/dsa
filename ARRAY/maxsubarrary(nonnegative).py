def max_non_negative_subarray(arr):
    max_sum = -1
    max_subarray = []
    
    current_sum = 0
    current_subarray = []
    
    for num in arr:
        if num >= 0:
            current_sum += num
            current_subarray.append(num)
        else:
            if (current_sum > max_sum) or (current_sum == max_sum and len(current_subarray) > len(max_subarray)):
                max_sum = current_sum
                max_subarray = current_subarray[:]
            current_sum = 0
            current_subarray = []
    
    #last check 
    if (current_sum > max_sum) or (current_sum == max_sum and len(current_subarray) > len(max_subarray)):
        max_subarray = current_subarray[:]
    
    if not max_subarray:
        return -1
    return max_subarray
print(max_non_negative_subarray([1, 2, 3]))          
print(max_non_negative_subarray([-1, 2]))            
print(max_non_negative_subarray([1, 2, 5, -7, 2, 6])) 
print(max_non_negative_subarray([-1, -2, -3]))       
