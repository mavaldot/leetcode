
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 1);
        
        int prod = 1;
        for (int i = 1; i < n; i++) {
            prod *= nums[i-1];
            res[i] *= prod;
        }
        
        int rprod = 1;
        for (int i = n - 2; i >= 0; i--) {
            rprod *= nums[i+1];
            res[i] *= rprod;
        }
        
        return res;
    }
};