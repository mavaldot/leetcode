#include <vector>
#include <unordered_map>
#include <iostream>

using namespace std;


class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        
        unordered_map<int, int> m;
        
        return getSum(0, triangle, 0, 0, m);
        
    }
    
    int getSum(int sum, vector<vector<int>>& triangle, int r, int c, unordered_map<int, int>& m) {
        if (r >= triangle.size()) return 0;
        
        sum = triangle[r][c];
        
        int sumLeft = 0;
        int sumRight = 0;
        
        int left = 200*(r+1)+c;
        int right = 200*(r+1)+c+1;
        
        if (m.find(left) == m.end()) {
            sumLeft = getSum(sum, triangle, r+1, c, m);
            m[left] = sumLeft;
        }
        else {
            sumLeft = m[left];
        }
        
        if (m.find(right) == m.end()) {
            sumRight = getSum(sum, triangle, r+1, c+1, m);
            m[right] = sumRight;
        }
        else {
            sumRight = m[right];
        }
        
        sum += min(sumLeft, sumRight);
        
        cout << r << ":" << c << " - "<< sum << endl;
        
        return sum;
        
        
    }
    
};