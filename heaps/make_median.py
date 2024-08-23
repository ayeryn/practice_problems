# 3107

from heapq import *


def make_median(nums: list[int], k: int) -> int:
    """
    Median:
    - when len(nums) is odd, the (l//2)ith element
    - when len(nums) is even, the average of (l//2 - 1)th and (l//2)th element

    We need to make sure everything before median is <= k and everything after median >= k
    """
    heap = []
    size = len(nums) // 2 + 1

    for n in nums:
        heappush(heap, -n)
        if len(heap) > size:
            heappop(heap)

    # Now heap has the <size> smallest elements in nums
    # We need all those numbers to be <= k

    if -heap[0] == k:
        return 0

    # if odd - we c
    # FIXME: We really need to check all the elements in the list
    if len(heap) % 2:
        top = -heappop(heap)
        print(top)
        return abs(top - k)
    # if even - we care about the top 2
    else:
        t1 = -heappop(heap)
        t2 = -heappop(heap)
        print(t1, t2)
        return abs(t1 + t2 - k * 2)
