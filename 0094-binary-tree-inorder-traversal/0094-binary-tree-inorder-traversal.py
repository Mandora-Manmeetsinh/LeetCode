# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []

        def recTra(currentNode: Optional[TreeNode]) -> None:
            if currentNode is None:
                return
            recTra(currentNode.left)
            result.append(currentNode.val)
            recTra(currentNode.right)

        recTra(root)
        return result