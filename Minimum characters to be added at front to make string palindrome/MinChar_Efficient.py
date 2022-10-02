'''
LPS stands for Longest Prefix Suffix which is noting but a prefix of any string which is also a suffix.
This approach takes O(N) time.
'''

class Solution:
    def computeLPS(self, s):
        n = len(s)
        lps = [0] * n
    
        l = 0
        i = 1
        while i < n:
            if s[i] == s[l]:
                l += 1
                lps[i] = l
                i += 1
            else:
                if l !=0 :
                    l = lps[l-1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def minChar(self, s):
        l = len(s)
        s = s + '#' + s[::-1]
        lps = obj.computeLPS(s)
        return l - lps[-1]
       
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