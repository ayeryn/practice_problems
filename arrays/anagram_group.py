from collections import defaultdict

"""
TIP: dict or array cannot be the key of hashmap BUT tuple can
"""


def group(strs: list[str]) -> list[list[str]]:
    d = defaultdict(list)

    for s in strs:  # O(n)
        count = [0] * 26

        for c in s:  # O(len(s))
            count[ord(c) - ord("a")] += 1

        d[tuple(count)].append(s)

    return d.values()


def group_brute(strs: list[str]) -> list[list[str]]:
    ans = []
    d = defaultdict(list)
    cache = []

    def anagram(s):
        count = defaultdict(int)

        for c in s:
            count[c] += 1

        return count

    for s in strs:
        cache.append(anagram(s))

    for i in range(len(strs)):
        a = cache[i]  # O(len(s))
        added = False

        if i not in d:
            for k in d:  # worst case O(n)
                if cache[k] == a:
                    d[k].append(strs[i])
                    added = True
                    break

        if not added:
            d[i].append(strs[i])

    for k in d:
        ans.append(d[k])

    return ans
