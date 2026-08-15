class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(x1, y1, x2, y2):
            return abs(x1 - x2) + abs(y1 - y2)
        
        n = len(points)
        adj = {i:[] for i in range(n)}

        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                dist = distance(xi, yi, xj, yj)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        
        res = 0
        visit = set()
        minH = [[0, 0]] # starting at point 0 [cost, point]
        while len(visit) < n:
            cost, i = heapq.heappop(minH)
            if i in visit: # if we already visited point i
                continue
            
            res += cost
            visit.add(i)
            for neighCost, neigh in adj[i]:
                if neigh not in visit:
                    heapq.heappush(minH, [neighCost, neigh])
        
        return res


