import heapq


class MiddleElementFinder:
    def __init__(self):
        self.heaps = [], []  # min, max

    def add_num(self, num: int) -> None:
        # large in min heap
        # small in max heap
        if self.heaps[0] and num > self.heaps[0][0]:
            heapq.heappush(self.heaps[0], num)
        elif self.heaps[1] and num < -self.heaps[1][0]:
            heapq.heappush(self.heaps[1], -num)
        else:
            heapq.heappush(self.heaps[0], num)
        # print(f"Add num {num}, heaps = {self.heaps}")

        # Balance the heaps
        if len(self.heaps[0]) - len(self.heaps[1]) > 1:
            heapq.heappush(self.heaps[1], -heapq.heappop(self.heaps[0]))
        if len(self.heaps[1]) - len(self.heaps[0]) > 0:
            heapq.heappush(self.heaps[0], -heapq.heappop(self.heaps[1]))

        # print(f"Balanced: {self.heaps}")

    def middle_element(self) -> int:
        return self.heaps[0][0]
