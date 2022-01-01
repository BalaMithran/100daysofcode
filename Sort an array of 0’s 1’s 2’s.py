class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        lessthan1 = 0
        morethan1 = len(nums)-1
        while i <   morethan1+1  :
            if nums[i] == 1:
                i+=1
            elif nums[i] ==0 :
                nums[lessthan1] , nums[i] =  nums[i] , nums[lessthan1]
                lessthan1+=1
                i+=1
            elif nums[i] ==2  :
                nums[morethan1] , nums[i] =  nums[i] , nums[morethan1]
                morethan1-=1
                
            
        """
        Do not return anything, modify nums in-place instead.
        """
        