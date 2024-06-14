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

        # Balance the heaps
        if len(self.heaps[0]) - len(self.heaps[1]) >= 1:
            heapq.heappush(self.heaps[1], -heapq.heappop(self.heaps[0]))
        if len(self.heaps[1]) - len(self.heaps[0]) >= 1:
            heapq.heappush(self.heaps[0], -heapq.heappop(self.heaps[1]))

    def middle_element(self) -> int:
        return self.heaps[0][0]


# estimate_finder = MiddleElementFinder()
# estimate_finder.add_num(5)
# print(estimate_finder.heaps)
# estimate_finder.add_num(10)
# print(estimate_finder.heaps)
# estimate_finder.add_num(3)
# print(estimate_finder.heaps)
# estimate_finder.add_num(1)
# print(estimate_finder.heaps)
# estimate_finder.add_num(7)
# print(estimate_finder.heaps)
# estimate_finder.add_num(11)
# print(estimate_finder.heaps)
# estimate_finder.add_num(8)
# print(estimate_finder.heaps)
# estimate_finder.add_num(2)
# print(estimate_finder.heaps)

# print(estimate_finder.middle_element())  # Expected output: 5
