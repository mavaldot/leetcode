#include <vector>
#include <cstdio>
#include <iostream>

using namespace std;

int helper(vector<int>& nums, int target, int start, int end);

int search(vector<int>& nums, int target) {
    
    return helper(nums, target, 0, nums.size());
    
}

int helper(vector<int>& nums, int target, int start, int end) {
    
    int mid = (end + start) / 2;
    //mid++;
    printf("%d %d %d . ", start, mid, end);
    
    if (mid == end || start == mid) {
        cout << mid << " end " << end << " begin " << start;
        if (target == nums[mid]) return mid;
        return -1;
    }

    if (target == nums[mid]) return mid;
    
    if (target > nums[mid]) return helper(nums, target, mid, end);
    if (target < nums[mid]) return helper(nums, target, start, mid);
    
    
    return -1;
}

int main() {
    vector<int> v = {5};
    int x = search(v, 5);
    cout << endl << x;
}