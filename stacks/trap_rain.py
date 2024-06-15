def trap_rain(height: list[int]) -> int:
    left = 0
    ans = 0
    while left < len(height):
        # we can only trap water is there's an "opening" between edges
        if height[left]:
            right = left + 1
            while right < len(height) and not height[right]:
                right += 1

            if right < len(height):
                ans += (right - left - 1) * min(height[left], height[right])

            left = right
        else:
            left += 1

    return ans
