from collections import defaultdict


def two_int_sum(nums: list[int], target: int) -> list[int]:
    index_map = defaultdict(list)

    for i in range(len(nums)):  # O(n)
        index_map[nums[i]] = i

    for i in range(len(nums)):  # O(n)
        n = nums[i]
        diff = target - n

        if diff in index_map:  # O(1)
            if index_map[diff] != i:
                return [i, index_map[diff][0]]

            if len(index_map[diff]) > 1:
                return [i, index_map[diff][1]]


def two_int_sum_brute(nums: list[int], target: int) -> list[int]:
    for i in len(nums):
        for i in (i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
