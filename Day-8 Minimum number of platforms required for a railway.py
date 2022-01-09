
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,n,arr,dep):
        output = 1
        max_so_far = 1
        arr.sort()
        dep.sort()
        i = 1
        j = 0
        while i<n and j<n:
            if arr[i] <= dep[j]:
                output+=1
                i+=1
            else:
                output-=1
                j+=1
            max_so_far = max(max_so_far , output)
        return max_so_far


# Problem link
# https://practice.geeksforgeeks.org/problems/minimum-platforms-1587115620/1#