class Solution(object):
    def maxArea(self, h):
        
        ans,i,j = 0,0,len(h)-1

        while i < j :
            if h[i] <= h[j] :
                res = h[i] * (j-i)
                i += 1
            else :
                res = h[j] * (j-i)
                j -= 1

            if res > ans : ans = res

        return ans 