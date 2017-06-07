class Solution(object):
    def ArrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # your solution here
        pairSum = 0
        nums.sort()
        i = 0
        while i < len(nums):
        	pairSum += nums[i]
        	i += 2
        return pairSum
