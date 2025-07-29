class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)  # since one number is missing from 0 to n
        total_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        missing = total_sum - actual_sum
        return missing
