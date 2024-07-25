# 227

from collections import deque
from math import floor, ceil


def basic_calculator(s: str) -> int:
    ops1 = "+-"
    ops2 = "*/"
    i = 0
    stack = deque()
    num = ""

    def handle_ops2(num):
        nonlocal stack

        op_2 = int(num)
        op = stack.pop()
        op_1 = stack.pop()
        if op == "*":
            stack.append(op_1 * op_2)
        else:
            n = op_1 / op_2
            if n > 0:
                stack.append(floor(n))
            else:
                stack.append(ceil(n))

    while i < len(s):
        # Handle "*/"
        if s[i].isdigit():
            num += s[i]

            if i == len(s) - 1:
                if stack and stack[-1] in ops2:
                    handle_ops2(num)
                else:
                    stack.append(int(num))
        else:
            if num != "":  # push num on stack
                if stack and stack[-1] in ops2:
                    handle_ops2(num)
                else:
                    stack.append(int(num))
                num = ""

            if s[i] in ops1 or s[i] in ops2:
                stack.append(s[i])

        i += 1

    while len(stack) > 1:
        # Handle "+-"
        op_1 = stack.popleft()
        op = stack.popleft()
        op_2 = stack.popleft()
        if op == "+":
            stack.appendleft(op_1 + op_2)
        else:
            stack.appendleft(op_1 - op_2)

    return stack[0]
