def three_sum(nums: list[int]) -> list[list[int]]:
    ans = set()  # Avoid duplicates
    nums.sort()
    x = 0

    while x < len(nums) and nums[x] <= 0:  # O(n)
        # x has to be negative or 0 to yield a solution

        left, right = x + 1, len(nums) - 1

        while left < right:  # O(n)
            if nums[left] + nums[right] == -nums[i]:
                ans.add((nums[x], nums[left], nums[right]))
                left += 1
                right -= 1
            elif nums[left] + nums[right] > -nums[x]:
                right -= 1
            else:
                left += 1
        x += 1

    return ans
