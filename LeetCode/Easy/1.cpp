/*
* 1. Two Sum
*/
#include <iostream>
#include <vector>
#include <unordered_map>

using std::vector;
using std::unordered_map;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> sums;
        for (int i = 0; i < nums.size(); i++) {
            if (sums.find(target - nums[i]) != sums.end()) {
                return vector<int> {i, sums[target - nums[i]]};
            }
            sums[nums[i]] = i;
        }
        return {};
    }
};