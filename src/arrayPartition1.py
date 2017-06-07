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
# sol = Solution()
# print(sol.ArrayPairSum([1,2,3,4,5,6]))
