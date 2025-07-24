class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        full_set = set(range(1, n + 1))  # All numbers from 1 to n
        nums_set = set(nums)             # Existing numbers in the list
        
        result = list(full_set - nums_set)  # Missing = all - existing
        return result
