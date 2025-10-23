class Solution:
    def hasSameDigits(self, s: str) -> bool:
        return (f:=lambda q:f([sum(p)%10 for p in pairwise(q)]) if len(q)>2 else eq(*q))([*map(int,s)])