class Solution(object):
    def ArrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # your solution here
        pairSum = 0
        nums.sort()
        for i in range (0, len(nums)//2+1):
        	pairSum += nums[i]
        return pairSum

