from collections import defaultdict


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
