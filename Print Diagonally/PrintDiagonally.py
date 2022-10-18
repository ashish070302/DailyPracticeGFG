#User function Template for python3

def downwardDigonal(N, A): 
    # code here 
    map = {}
    for row in range(N):
        for coloumn in range(N):
            key = row + coloumn
            if key not in map:
                map[key] = []
            map[key].append(A[row][coloumn])

    output = []
    key = 0
    while key in map:
        output += map[key]
        key += 1
    return output
  
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDigonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

# } Driver Code Ends