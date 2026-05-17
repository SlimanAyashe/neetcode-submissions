# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        temp = root
        result =  -1
        while stack or temp or k>0:
            while temp:
                stack.append(temp)
                temp = temp.left
            
            temp = stack.pop()
            k -= 1 
            if k == 0:
                result = temp.val
            temp = temp.right

        return result