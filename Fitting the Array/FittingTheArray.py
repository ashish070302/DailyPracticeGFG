#User function Template for python3

class Solution:
    def isFit (self,arr, brr, n) : 
        #Complete the function
        arr.sort()
        brr.sort()
        l=0
        c=0
        for l in range(n):
            if(arr[l]<=brr[l]):
                c+=1
        if(c==n):
            return True
        else:
            return False
            
#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    brr = list(map(int, input().strip().split()))
    a=Solution()
    ans = a.isFit(arr, brr, n)
    if(ans == True):
        print("YES")
    else:
        print("NO")
# } Driver Code Ends