/*
* 380. Insert Delete GetRandom O(1)
*/
#include <iostream>
#include <vector>
#include <unordered_map>
#include <cstdlib>

using std::vector;
using std::unordered_map;

class RandomizedSet {
public:
    /** Initialize your data structure here. */
    RandomizedSet() {}
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if (randomSet.find(val) == randomSet.end()) {
            arr.push_back(val);
            randomSet[val] = arr.size() - 1;
            return true;
        }
        return false;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if (randomSet.find(val) != randomSet.end()) {
            int last = arr.back();
            // Swap index of map, as we prepare to overwrite
            randomSet[last] = randomSet[val];
            // Overwrite element to be removed with last element
            arr[randomSet[last]] = last;
            arr.pop_back();
            randomSet.erase(val);
            return true;
        }
        return false;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        return arr[rand() % arr.size()];
    }

private:
    vector<int> arr;
    unordered_map<int, int> randomSet;
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */