#set mismatch 645 

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        for num in nums:
            index=abs(num)-1 

            if nums[index]<0:
                res.append(abs(num))
            else:
                nums[index]*=-1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                # Missing number
                res.append(i + 1)
        
        return res