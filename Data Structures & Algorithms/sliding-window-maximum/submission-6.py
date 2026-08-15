class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
       
        """
        nlogn time??
        n -> linear search
        nlogn -> linear search, with binary search at each step?

        what do we know:
        at each step:
        - the previous k - 1 elements in the window
        - the INDEX of the previous maximum
        - the maximum of the previous


        example:
        [1,2,1,0,4,2,6] 
        [0,1,1,2,2,4,6] <- what if we sorted, and popped the 
        """

        heap = []
        res = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        res.append(-heap[0][0])
        l = 1
        for r in range(k, len(nums)):
            heapq.heappush(heap, (-nums[r], r))
            while heap and heap[0][1] < l:
                heapq.heappop(heap)
            res.append(-heap[0][0])
            l += 1
        
        return res

        
