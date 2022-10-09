#User function Template for python3
import math
class Solution:

	def isPrime(self, N):
        k = int(math.sqrt(N)) + 1
        for i in range(2, k, 1):
            if (N % i == 0):
                return False
        return True
  
    def NthTerm(self, N):
    		# Code here
        if (N == 0):
            return 2
        elif (N == 1):
            return 1
        elif (ob.isPrime(N)):
            return 0
     
        aboveN = -1
        belowN = -1
             
        n1 = N + 1
        while (True):
            if (ob.isPrime(n1)):
                aboveN = n1
                break
            else:
                n1 += 1
     
        n1 = N - 1
        while (True):
            if (ob.isPrime(n1)):
                belowN = n1
                break  
            else:
                n1 -= 1
     
        diff1 = aboveN - N
        diff2 = N - belowN
     
        return min(diff1, diff2)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.NthTerm(N)
		print(ans)

# } Driver Code Ends

#Contibuted by Ashish Kumar