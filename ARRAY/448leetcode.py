#448. Find All Numbers Disappeared in an Array
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            index=abs(num)-1
            nums[index]=abs(nums[index])*-1
        
        res=[]
        for index,num in enumerate(nums):
            if num>0:
                res.append(index+1)

        return res