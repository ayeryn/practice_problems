def three_sum(nums: list[int]) -> list[list[int]]:
    ans = []
    nums.sort()
    x = 0

    while x < len(nums) and nums[x] <= 0:  # O(n)
        # x has to be negative or 0 to yield a solution
        if x > 0 and nums[x] == nums[x - 1]:
            x += 1
            continue

        left, right = x + 1, len(nums) - 1

        while left < right:  # O(n)
            if nums[left] + nums[right] == -nums[x]:
                ans.add((nums[x], nums[left], nums[right]))
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    # Avoid duplicates
                    left += 1
                # The next iteration will take care of decreasing right
            elif nums[left] + nums[right] > -nums[x]:
                right -= 1
            else:
                left += 1
        x += 1

    return ans
