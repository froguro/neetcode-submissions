class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.timeMap[key]
        if not values:  # Key doesn't exist
            return ""

        l = 0
        r = len(values) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            value = values[mid][0]
            time = values[mid][1]
            if timestamp < time:
                r = mid - 1
            else:
                res = value
                l = mid + 1

        
        return res
        
