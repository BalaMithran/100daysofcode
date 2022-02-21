class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.helper(root,arr)
        return arr
    def helper(self,root,arr):
        if root:
            arr.append(root.val)
            self.helper(root.left,arr)
            self.helper(root.right,arr)
            
   
  # Problem link
  # https://leetcode.com/problems/binary-tree-preorder-traversal/
