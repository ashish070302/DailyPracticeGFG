'''
A simple solution is to check if the string is already a palindrome string.
The problem with this that if the procedure isPalindrome() has time complexity 
of O(n) which is being called with each iteration of the while loop the overall 
time complexity of the loop becomes O(n^2).
'''
class Solution:  
    def is_palindrome(self, s):
        if s == s[::-1]:
            return True
        return False

    def minChar(self, s):
        f = False
        ctr = 0
        while len(s) > 0:
            if obj.is_palindrome(s):
                f = True
                break
            else:
                ctr += 1
                s = s[0:len(s)-1]
        return ctr
       
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        s=input()
        obj=Solution()
        ans=obj.minChar(s)
        print(ans)
# } Driver Code Ends

#Code contributed by Ashish Kumar