class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        res = 0
        points.sort(key=lambda p: (p[0], -p[1]))
        for i, (x, y) in enumerate(points):
            maxY = -inf
            for (bobX, bobyY) in points[i + 1:]:
                if maxY < bobyY <= y:
                    res += 1
                    maxY = bobyY
        return res 