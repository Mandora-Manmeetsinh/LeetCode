class Solution(object):
    def answerString(self, word, numFriends):
        if numFriends == 1:
            return word
        
        n = len(word)
        max_len = n - numFriends + 1
        max_char = max(word)
        
        best = ""
        for i, ch in enumerate(word):
            if ch == max_char:
                candidate = word[i:i + max_len]
                if candidate > best:
                    best = candidate
        return best