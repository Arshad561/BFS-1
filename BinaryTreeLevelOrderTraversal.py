# Time Complexity: O(N), N is the number of nodes in the tree
# Space Complexity: O(N)
# Did this code successfully run on Leetcode: Yes


from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        if root is None:
            return result

        queue = deque()
        queue.append(root)

        while len(queue):
            size = len(queue)
            li = []

            for _ in range(size):
                popped = queue.popleft()
                li.append(popped.val)

                if popped.left:
                    queue.append(popped.left)
                
                if popped.right:
                    queue.append(popped.right)
            
            result.append(li)
        
        return result
        