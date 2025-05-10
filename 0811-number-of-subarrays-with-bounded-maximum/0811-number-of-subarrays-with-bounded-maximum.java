class Solution {
    public int numSubarrayBoundedMax(int[] nums, int left, int right) {
        int len = nums.length;

        if (len == 0) {
            return 0;
        }

        int ans = 0;
        int n = 0;
        int i = 0;
        int s = 0;

        while (i < len) {
            if (nums[i] > right) {
                n = 0;
                s = 0;
            } else if (nums[i] < left) {
                s++;
                n++;
            } else {
                s = 0;
                n++;
            }
            ans = ans + n - s;
            i++;
        }
        return ans;
    }
}