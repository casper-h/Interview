/*
* 78. Subsets
*/
#include <iostream>
#include <vector>
#include <algorithm>

using std::vector, std::sort;

class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        // We start with the empty set [[]]
        vector<vector<int>> answer(1, vector<int>());

        for (int i = 0; i < nums.size(); i++) {
            int subset = answer.size();
            for (int j = 0; j < subset; j++) {
                // We push for a new subsets [[], []]
                answer.push_back(answer[j]);
                // Add the unique number [[], [1]]
                answer.back().push_back(nums[i]);
            }
        }
        return answer;
    }
};