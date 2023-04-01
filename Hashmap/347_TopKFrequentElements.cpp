#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
       unordered_map<int, int> map;
        
        vector<int> v;
        
        for (int& num : nums) {
            map[num]++;
        }
        
        while (k-- > 0) {
            int max = 0;
            int most_frequent = 0;
            for (auto& item : map) {
                if (item.second > max) {
                    max = item.second;
                    most_frequent = item.first;
                }
            }
            
            map.erase(most_frequent);
            v.push_back(most_frequent);
        }
        
        return v;
    
    }
};