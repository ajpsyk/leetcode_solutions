from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # create a tuple key -> (timestamp, value) and append to timeMap
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        # binary search in key array
        timestamps = self.timeMap[key]
        value = ""
        if not timestamps:
            return value
        start = 0
        end = len(timestamps) - 1
        while start <= end:
            middle = start + (end - start) // 2
            t, v = timestamps[middle]
            if t <= timestamp:
                value = v
                start = middle + 1
            else:
                end = middle - 1
        return value
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)