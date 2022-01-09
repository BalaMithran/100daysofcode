class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        timings = [(start[i], end[i]) for i in range(n)]
        count , end_of_prev = 0,0
        timings.sort(key=lambda x:x[1])
        for i in range(n):
            if timings[i][0] > end_of_prev:
                count+=1
                end_of_prev = timings[i][1]
        return count


# Problem Link
# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1