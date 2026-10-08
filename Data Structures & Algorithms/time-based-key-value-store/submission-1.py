import bisect
class TimeMap:

    def __init__(self):
        self.timemp = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemp[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemp:
            return ""
        if self.timemp[key][0][0]>timestamp:
            return ""
        index = bisect.bisect_right(self.timemp[key], timestamp, key=lambda x: x[0])
        return self.timemp[key][index-1][1]
