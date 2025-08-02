class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        dicthash={}
        ans=[]
        for i in nums:
            if i in dicthash:
                ans.append(i)
            else:
                dicthash[i]=1 
        return list(map(int,ans))[0]