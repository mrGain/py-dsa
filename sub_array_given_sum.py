#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
# class Solution:
#     def subArraySum(self,arr, n, s): 
#         #Write your code here
        
#         for i in range(n):
#             sum_arr = 0
#             if arr[i] == s:
#                 return [i, i]

#             for j in range(i,n):
#                 sum_arr = sum_arr + arr[j]
#                 if sum_arr == s:
#                     return [i+1, j+1]

#         return [-1]            
class Solution:
   def subArraySum(self,arr, n, s): 
      #Write your code here
       for i in range(n-1):
           total = 0
           for j in range(1,n):               #step1
               if sum(arr[i:j+1])==s:         #step2
                   return [i+1,j+1]             #step3
       return [-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            print(ans)
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends