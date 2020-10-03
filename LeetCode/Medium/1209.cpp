/*
* 1209. Remove All Adjacent Duplicates in String II
*/
#include <iostream>
#include <string>
#include <vector>
#include <utility>

using std::string;
using std::vector;
using std::pair;

class Solution {
public:
    string removeDuplicates(string s, int k) {
        string answer;
        // Use a "stack"
        vector<pair<char, int>> stack;
        for (int i = 0; i < s.size(); i++) {
            // If the stack is empty OR current char is different from last char
            if (stack.empty() || stack.back().first != s[i]) {
                stack.push_back({s[i], 0});
            }
            // Increment, as the same char appeared again
            stack.back().second++;
            // If the "top" of the stack has shown k times, pop
            if (stack.back().second == k) {
                stack.pop_back();
            }
        }
        for (int i = 0; i < stack.size(); i++) {
            answer += string(stack[i].second, stack[i].first);
        }
        return answer;
    }
};