class Solution {
    public int maxProfit(int[] prices) {
        int maxi = Integer.MAX_VALUE;
        int ans = 0;
        int ans1 = 0;
        
        for(int i = 0; i < prices.length; i++){
            if(prices[i] < maxi){
                maxi = prices[i];
            }
            ans1 = prices[i] - maxi;
            if( ans < ans1){
                 ans = ans1;
            }
        }
        return  ans;
    }
}