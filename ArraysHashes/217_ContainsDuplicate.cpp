
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map<int, int> map;
        for (auto& x : nums) {
            map[x]++;
            if (map[x] % 2 == 0) return true;
        }
        return false;
    }
};