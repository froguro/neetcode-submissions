class TimeMap:

    def __init__(self):
        self.timeMapping = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMapping[key] = self.timeMapping.get(key, []) + [[value, timestamp]]
        

    def get(self, key: str, timestamp: int) -> str:
        # binary search cuz
        # timestamps are strictly increasing
        # return prev_timestamp, the most recent timestamp
        # but prev_timestamp has to be less than timestamp
        # [1, 3], timestamp = 3
        if key not in self.timeMapping:
            return ""
        
        l, r = 0, len(self.timeMapping[key]) - 1

        while l <= r:
            mid = (l + r) // 2
            if self.timeMapping[key][mid][1] == timestamp:
                return self.timeMapping[key][mid][0]
            
            prev_timestamp = self.timeMapping[key][mid][1]

            if prev_timestamp > timestamp:
                r = mid - 1
            else:
                l = mid + 1
            
        
        return self.timeMapping[key][l - 1][0] if self.timeMapping[key][l - 1][1] <= timestamp else ""
