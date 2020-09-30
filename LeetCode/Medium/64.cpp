/*
* 64. Minimum Path Sum
*/
#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using std::min;

class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size(), n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    // Where you start (0, 0)
                    dp[i][j] = grid[i][j];
                } else if (i == 0 && j != 0) {
                    // First row, you can only come from the "left" + current (i, j)
                    dp[i][j] = dp[i][j - 1] + grid[i][j];
                } else if (j == 0 && i != 0) {
                    // First column, you can only come from the "top" + current (i, j)
                    dp[i][j] = dp[i - 1][j] + grid[i][j];
                } else {
                    // You find min of "left" or "top" + current (i, j)
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j];
                }
            }
        }
        return dp[m - 1][n - 1];
    }
};