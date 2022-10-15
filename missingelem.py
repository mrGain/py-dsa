#User function Template for python3


class Solution:
    def MissingNumber(self,array,n):
        total = n*(n+1)/2
        sum_arr = 0
        for i in range(n -1):
            sum_arr = sum_arr + array[i]

        return int(total - sum_arr)    


#{ 
 # Driver Code Starts
#Initial Template for Python 3




t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    s=Solution().MissingNumber(a,n)
    print(s)
# } Driver Code Ends