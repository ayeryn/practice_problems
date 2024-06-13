from collections import defaultdict


"""
A sneaky way to implement bucket sort

Normally, bucket sort initializes an array for each i in nums.
Here we use freq to store elements that appears i times. Since an element can appear at most len(nums) times so filling out freq takes linear time.
"""


def top_k(nums: list[int], k: int) -> list[int]:
    freq = [[] for _ in range(len(nums) + 1)]
    count = defaultdict(int)

    for n in nums:  # O(n)
        count[n] += 1

    for key in count:  # O(n)
        c = count[key]
        freq[c].append(key)

    ans = []
    # Iterate backwards to get most frequent
    # if least frequent we can iterate forward
    for i in range(len(nums), -1, -1):  # O(n)
        if freq[i] > 0:
            ans.extend(freq[i])

        if len(ans) == k:
            return ans


def top_k_sorted(nums: list[int], k: int) -> list[int]:
    d = defaultdict(int)

    for n in nums:  # O(n)
        d[n] += 1

    # O(nlogn)
    l = sorted([(v, k) for k, v in d.items()], reverse=True)

    ans = []
    i = 0

    while i < k:  # O(k)
        ans.append(l[i][1])
        i += 1
    return ans
