/*
* 1249. Minimum Remove to Make Valid Parentheses
*/
#include <iostream>
#include <string>
#include <stack>

using std::string;
using std::stack;

class Solution {
public:
    string minRemoveToMakeValid(string s) {
        // This is similar to checking parentheses in general
        stack<int> invalid;
        for (int i = 0; i < s.size(); i++) {
            // If we see a '('
            if (s[i] == '(') {
                invalid.push(i);
            }
            if (s[i] == ')') {
                // If we see a ')' and the stack is not empty, as empty means out of place
                if (!invalid.empty()) {
                    invalid.pop();
                } else {
                    s[i] = '*';
                }
            }
        }
        // Remaining stack elements are all out of place
        while (!invalid.empty()) {
            s[invalid.top()] = '*';
            invalid.pop();
        }
        s.erase(remove(s.begin(), s.end(), '*'), s.end());
        return s;
    }
};