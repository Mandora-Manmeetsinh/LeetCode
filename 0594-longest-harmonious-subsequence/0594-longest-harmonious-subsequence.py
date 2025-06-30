class Solution(object):
    def findLHS(self, nums):
        nums.sort()
        j = 0
        maxL = 0

        for i in range(len(nums)) :
            while nums[i] - nums[j] > 1 :
                j += 1
            if nums[i] - nums[j] == 1 :
                maxL = max(maxL , i-j+1)
        return maxL