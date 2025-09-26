class Solution:
    def minInsertions(self, s: str) -> int:
        memo = {}
        n = len(s)
        def dfs(i,j):
            if i>=j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if s[i]==s[j]:
                memo[(i,j)] = dfs(i+1,j-1)
                return memo[(i,j)]
            else:
                memo[(i,j)] = min((1+dfs(i+1,j)),(1+dfs(i,j-1)))
                return memo[(i,j)]
        return dfs(0,n-1)