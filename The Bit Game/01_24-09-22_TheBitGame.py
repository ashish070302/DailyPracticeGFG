#User function Template for python3

class Solution:
    def swapBitGame (self,N):
        n=int((bin(N)[2:]))
        count = 0
        while (N):
            count += N & 1
            N >>= 1
            b=count
        if (b%2==0):
            return 2
        else:
            return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N=int(input())
        

        ob = Solution()
        print(ob.swapBitGame(N))
# } Driver Code Ends