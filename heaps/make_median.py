# 3107

from heapq import *


def make_median(nums: list[int], k: int) -> int:
    if len(nums) == 1:
        return abs(k - nums[0])

    heap = []
    for n in nums:
        heappush(heap, n)

    """
    We need to make sure that:
    1. everything before median is <= k
    2. median == k
    3. everything after median is >= k

    Note: based on description of problem, median is at l//2 regardless of len(nums)
    """

    steps = 0
    l = len(heap)
    # heap[:l//2] <= k, heap[l//2] == k, heap[l//2+1:] >= k
    i = 0
    while heap:
        curr = heappop(heap)
        if i < l // 2:  # before
            if curr > k:
                steps += curr - k
        elif i == l // 2:  # median
            if curr != k:
                steps += abs(curr - k)
        else:  # after
            if curr < k:
                steps += k - curr
        i += 1

    return steps
