class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index ,val  in enumerate(nums):
            diff = target-val
            if diff in nums and nums.index(diff)!=index:
                return (index , nums.index(diff))
         
        
# Problem link
# https://leetcode.com/problems/two-sum/