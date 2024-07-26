# 94

from typing import Optional
from TreeNode import TreeNode


def traverse(root: Optional[TreeNode]) -> list[int]:
    """inorder: left -> node -> right"""

    if not root:
        return []

    stack = [root]
    nodes = []

    while stack:
        if stack[-1].left:  # left
            stack.append(stack[-1].left)
        else:
            curr = stack.pop()  # node
            nodes.append(curr.val)

            while stack and not curr.right:
                # keep popping until we have a node with right child
                curr = stack.pop()
                nodes.append(curr.val)

            if curr.right:  # right
                stack.append(curr.right)

    return nodes
