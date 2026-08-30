class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (r + l) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / k)
            if time <= h:
                res = k
                r = k - 1
            elif time > h:
                l = k + 1

        return res