class Solution {
    public int reverse(int x) {
       long p = x;
       long maxInt = Integer.MAX_VALUE;
       long minInt = Integer.MIN_VALUE;
       long m=p%10;
       long n=p/10;
       while(n!=0){
        long t= n%10;
        m=m*10;
        m=m+t;
        n=n/10;

        if (m > maxInt || m < minInt ) {
                return 0;
        }
       }
       int k= (int) m;
     
       return k;
    }
}