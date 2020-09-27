/*
* 1029. Two City Scheduling
*/
#include <iostream>
#include <vector>
#include <algorithm>

using std::vector, std::sort;

class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        /*
        * Total cost for sending everyone to City A, then find the difference of
        * sending everyone to City B.
        */
        int minCost = 0;
        vector<int> refund;
        for (const auto &cost : costs) {
            minCost += cost[0];
            refund.push_back(cost[1] - cost[0]);
        }

        // We only need to send n people, then just find maximum return from refunds
        sort(refund.begin(), refund.end());
        for (int i = 0; i < costs.size()/2; i++) {
            minCost += refund[i];
        }
        return minCost;
    }
};