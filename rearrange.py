class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0] * n
        
        posIndex = 0  # Even index for positive
        negIndex = 1  # Odd index for negative

        for num in nums:
            if num > 0:
                result[posIndex] = num
                posIndex += 2
            else:
                result[negIndex] = num
                negIndex += 2
        
        return result
