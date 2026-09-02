class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap[key]
        if not values:
            return ""

        l = 0
        r = len(values) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            if timestamp < values[mid][1]:
                r = mid - 1
            else:
                l = mid + 1
                res = values[mid][0]
        

        return res
        


        
