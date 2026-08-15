class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        h >= piles.length
        ceil(x / k) is how long it takes to eat x banana pile with k rate
        """

        n = len(piles)
        m = max(piles) # one pile per hour guaranteed

        lo = 1
        hi = m
        res = hi
        while lo <= hi:
            k = (lo + hi) // 2
            time = 0
            for x in piles:
                time += math.ceil(float(x) / k)
            if time <= h:
                res = k
                hi = k - 1
            else:
                lo = k + 1
        return res


