
                
        
            
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_local = 0
        max_global = nums[0]
        for i in nums:
            max_local = max(max_local+i , i)
            
            if max_local > max_global :
                max_global =max_local
        return max_global 
                
                
                


# A bit more elegant solution

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_local = 0
        max_global = nums[0]
        for i in nums:
            max_local = max(max_local+i , i)
            max_global = max(max_global,max_local)
        return max_global 
                
                
                
# Problem link
# https://leetcode.com/problems/maximum-subarray/
        