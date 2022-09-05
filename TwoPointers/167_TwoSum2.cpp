
#include <string>
#include <iostream>
#include <vector>

using namespace std;


class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;
        
        vector<int> sol = {1, 2};
        
        while (l < r) {
            if (l == r) {
                return sol;
            }
            int sum = numbers[l] + numbers[r];
            
            cout << sum;
            
            if (sum == target) {
                sol[0] = l + 1;
                sol[1] = r + 1;
                return sol;
            }
            
            if (sum > target) {
                r--;
            }
            else {
                l++;
            }
            
        }
        
        return sol;
    }
};