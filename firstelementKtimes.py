#User function Template for python3


class Solution:
    def largestElem(self,a):
        self.large = 0
        for i in range(len(a)):
            if a[i]>self.large:
                self.large = a[i]
        return self.large 

    def firstElementKTime(self,  a, n, k):
        # code here
        large = self.largestElem(a)
        hash = [0]*(large+1)
        for i in range(len(a)):
            temp = a[i]
            hash[temp] += 1

            if hash[temp] == k:
                return temp
        
        return -1            
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, k = sz[0], sz[1]
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.firstElementKTime(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends