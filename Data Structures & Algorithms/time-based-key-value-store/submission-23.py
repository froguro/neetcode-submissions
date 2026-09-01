class TimeMap:

    def __init__(self):
        self.tMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tMap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.tMap[key]
        if len(values) == 0:
            return ""

        l = 0
        r = len(values) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            if values[mid][1] < timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
            
        return res
        
