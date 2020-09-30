/*
* 62. Unique Paths
*/
#include <iostream>
#include <vector>

using std::vector;

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector<vector<int>> dp(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || j == 0) {
                    // Only 1 way to reach the first row/col
                    dp[i][j] = 1;
                } else {
                    // You find the "left" and "top"
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1];
                }
            }
        }
        return dp[m - 1][n - 1];
    }
};