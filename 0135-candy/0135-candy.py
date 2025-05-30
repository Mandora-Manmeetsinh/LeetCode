class Solution:
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n

        for i in range(1,n) :
            if ratings[i - 1] < ratings[i] and candies[i - 1] >= candies[i]:
                candies[i] = candies[i-1] + 1

        for i in range(n-2,-1,-1) :
            if ratings[i + 1] < ratings[i] and candies[i + 1] >= candies[i]:
                candies[i] = candies[i+1] + 1
        
        totel = sum(candies)
        return totel