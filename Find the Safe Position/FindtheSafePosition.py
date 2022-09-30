#User function Template for python3

class Solution:
    def safePos(self, n, k):
        # code here 
        if n == 1:
            return 1
        else:
            return (ob.safePos(n-1, k) + k-1) % n+ 1

#Code contibuted by Ashish Kumar
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n,k=map(int,input().split())
        
        ob = Solution()
        print(ob.safePos(n,k))
# } Driver Code Ends