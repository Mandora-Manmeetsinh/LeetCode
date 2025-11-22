class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        st=set()
        c=0
        for x in range(len(s)-2):
            if s[x] not in st:
                idx=len(s) - 1 - s[::-1].index(s[x])
                if idx!=x:
                    c=c+len(set(s[x+1:idx]))
                    st.add(s[x])
                else:
                    continue
        return c