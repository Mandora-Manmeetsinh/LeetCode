# class Solution(object):
#     def clearStars(self, s):

        # # print(s)
        # s = list(s)
        # st = '*'
        # if st in s :
        #     s.remove(st)
        #     s1 = str(s)
        #     return s
        # else :
        #     # print(s)
        #     s1 = str(s) 
        #     return s

class Solution:
    def clearStars(self, s):
        heap = []
        for i,c in enumerate(s):
            if c=='*':
                heappop(heap)
            else:
                heappush(heap,(ord(c),-i))
        
        ans = ['']*len(s)
        while heap:
            ordChar,i = heappop(heap)
            ans[-i] = chr(ordChar)
            
        return ''.join(ans)