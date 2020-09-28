/*
* 1047. Remove All Adjacent Duplicates In String
*/
#include <iostream>
#include <string>

using std::string;

class Solution {
public:
    string removeDuplicates(string S) {
        int i = 0;
        // i = next output char (what we are "looking" at)
        // j = iteration of input char
        for (int j = 0; j < S.size(); i++, j++) {
            S[i] = S[j];
            // k = 2, can always expand for k = n, "aaa"
            if (i > 0 && S[i] == S[i - 1]) {
                i -= 2;
            }
        }
        return S.substr(0, i);
    }
};