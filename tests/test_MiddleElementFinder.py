from heaps.MiddleElementFinder import MiddleElementFinder
import random


def test_1():
    nums = [random.randint(1, 50) for _ in range(15)]

    f = MiddleElementFinder()
    for n in nums:
        f.add_num(n)

    ret = f.middle_element()
    ans = sorted(nums)[len(nums) // 2]

    assert ret == ans
