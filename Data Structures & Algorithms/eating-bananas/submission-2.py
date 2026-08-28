class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            mid = (l + r) // 2
            time = 0 
            for x in piles:
                time += math.ceil(float(x) / mid)
            if time <= h:
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        
        return res