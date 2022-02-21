class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.helper(root,arr)
        return arr
    def helper(self,root,arr):
        if root:
            self.helper(root.left,arr)
            self.helper(root.right,arr)
            arr.append(root.val)
            
            
 
#Problem link
# https://leetcode.com/problems/binary-tree-postorder-traversal/
