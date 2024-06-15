def trap_rain(height: list[int]) -> int:
    ans = 0

    # Keep track of the max height on both sides excluding itself
    max_left = [0] * len(height)
    max_right = [0] * len(height)

    for i in range(1, len(height)):
        max_left[i] = max(max_left[i - 1], height[i - 1])

    for i in range(len(height) - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], height[i + 1])

    for i in range(len(height)):
        # Area is bounded by the smaller edge
        min_lr = min(max_left[i], max_right[i])
        if min_lr - height[i] >= 0:
            ans += min_lr - height[i]

    return ans


def trap_rain_two_pointer(height):
    ans = 0
    l, r = 0, len(height) - 1
    lm, rm = height[0], height[-1]

    while l < r:
        # Area is bound by the smaller edge
        m = min(lm, rm)

        # Update ans only when we update lm or rm
        if lm < rm:
            # Calculate water for left when we move forward
            if m - height[l] >= 0:
                ans += m - height[l]
            l += 1
            lm = max(lm, height[l])
        else:
            # Calculate water for right when we move backward
            if m - height[r] >= 0:
                ans += m - height[r]
            r -= 1
            rm = max(rm, height[r])

    return ans
