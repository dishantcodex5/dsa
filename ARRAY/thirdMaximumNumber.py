class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_array = list(set(nums))       # Remove duplicates
        new_array.sort(reverse=True)      # Sort in descending order

        if len(new_array) < 3:
            return new_array[0]           # Return max if less than 3 unique elements
        else:
            return new_array[2]           # Return 3rd max (0-based index)
