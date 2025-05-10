class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int left = 0, right = 0, sum = 0, minLength = Integer.MAX_VALUE;
        for (int num: nums) {
            sum += num;
            while (sum >= target) {
                minLength = Math.min (minLength, right - left + 1);
                sum -= nums[left++];
            }
            right++;
        }
        return minLength == Integer.MAX_VALUE ? 0 : minLength;       
    }
}