#Find All Duplicates in an Array

class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dicthash={}
        ans=[]

        for num in nums:
            if num in dicthash:
                ans.append(num)
            else:
                dicthash[num]=1
        return ans

        