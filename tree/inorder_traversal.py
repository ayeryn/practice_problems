# 94

from typing import Optional
from TreeNode import TreeNode


def traverse(root: Optional[TreeNode]) -> list[int]:
    """inorder: left -> node -> right"""

    if not root:
        return []

    stack = [root]
    nodes = []
    seen = set()

    while stack:
        # print(stack[-1].val, [n.val for n in stack], [n.val for n in seen])
        seen.add(stack[-1])

        if stack[-1].left and stack[-1].left not in seen:  # left
            seen.add(stack[-1].left)
            stack.append(stack[-1].left)
        else:
            curr = stack.pop()
            nodes.append(curr.val)  # node
            if curr.right:  # right
                stack.append(curr.right)
            else:
                while stack and not stack[-1].right:
                    nodes.append(stack.pop().val)

    return nodes


# root = TreeNode(3)
# left = TreeNode(1)
# right = TreeNode(2)
# root.left = left
# root.right = right

# print(traverse(root))
