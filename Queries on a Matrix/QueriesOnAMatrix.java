//{ Driver Code Starts
// Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;
class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br =
            new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out=new PrintWriter(System.out);
        int T = Integer.parseInt(br.readLine().trim());
        while (T-- > 0) {
            String[] s = br.readLine().trim().split(" ");
            int n = Integer.parseInt(s[0]);
            int q = Integer.parseInt(s[1]);
            int[][] Queries = new int[q][4];
            for (int i = 0; i < q; i++) {
                String[] s1 = br.readLine().trim().split(" ");
                for (int j = 0; j < 4; j++)
                    Queries[i][j] = Integer.parseInt(s1[j]);
            }
            Solution obj = new Solution();
            int[][] ans = obj.solveQueries(n, Queries);
            for (int i = 0; i < ans.length; i++) {
                for (int j = 0; j < ans[i].length; j++) {
                    out.print(ans[i][j] + " ");
                }
                out.println();
            }
        }
        out.close();
    }
}

// } Driver Code Ends


class Solution {
    public int[][] solveQueries(int n, int[][] Queries) {
        // Code here
        int[][] my_mat = new int[n][n];
        for(int[] q : Queries) {
            int a = q[0];
            int b = q[1];
            int c = q[2];
            int d = q[3];
            for(int row = a; row <= c; row++){
                my_mat[row][b]++;
                if(d+1 < n) 
                {
                    my_mat[row][d+1]--;
                }
            }
        }
        for(int col = 1; col < n; col++){
            for(int row = 0; row < n; row++){
                my_mat[row][col] += my_mat[row][col-1];
            }
        }

        return my_mat;
    }
}