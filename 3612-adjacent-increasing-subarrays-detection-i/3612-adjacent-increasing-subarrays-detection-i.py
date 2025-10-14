class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        n = len(nums)
        incr = [1]*n
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                incr[i] = incr[i-1]+1
        for i in range(k, n):
            if incr[i] >= k and incr[i-k] >= k:
                return True
        return False