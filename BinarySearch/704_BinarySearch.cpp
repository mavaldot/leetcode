#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    int search(vector<int>& nums, int target) {
        return binarySearch(nums, target, 0, nums.size()-1);
    }
    
    int binarySearch(vector<int>& nums, int target, int l, int r) {
        
        if (l == r && nums[l] != target) {
            return -1;
        }
        
        int middle = (r + l) / 2;
        if (nums[middle] == target) {
            return middle;
        }
        else if (nums[middle] > target) {
            return binarySearch(nums, target, l, middle);
        }
        else {
            return binarySearch(nums, target, middle+1, r);
        }
        
        return -1;
                      
    }
    
};