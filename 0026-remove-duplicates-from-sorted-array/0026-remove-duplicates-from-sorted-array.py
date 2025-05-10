class Solution(object):
    def removeDuplicates(self, nums):
        i ,j = 0,1
        n = len(nums)
        while j<n:
            if nums[j] == nums[i]:
                j += 1
            else:
                nums[i+1] = nums[j]
                i += 1
                j += 1   
        return i+1