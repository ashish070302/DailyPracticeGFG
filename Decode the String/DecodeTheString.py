#User function Template for python3
class Solution:
    def decodedString(self, s):
        # code here
        a = []
        i = 0
        res = ''
        while (i < len(s)):
            if (s[i] == ']'):
                b = ''
                while (a[-1] != '['):
                    b = a.pop() + b
                a.pop()
                m = ''
                while (a and a[-1].isdigit()):
                    m = a.pop() + m
                res = b * int(m)
                a.append(res)
            else:
                a.append(s[i])
            i += 1
        if(res == ''):
            return s
        res = ''
        for i in range(len(a)):
            res = a[i] + res
        return res        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        
        ob = Solution()
        print(ob.decodedString(s))
# } Driver Code Ends

#Contributed by Ashish Kumar