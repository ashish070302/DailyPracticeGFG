#User function Template for python3


class Solution:

    def numsGame(self, N):
        # code here
        if (N & 1) == 1:
            return 0
        else:
            return 1


#{
# Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.numsGame(N))
# } Driver Code Ends
