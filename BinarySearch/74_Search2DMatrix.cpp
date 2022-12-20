#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        return searchForRow(matrix, target, 0, matrix.size()-1);
    }
    
    bool searchForRow(vector<vector<int>>& matrix, int target, int lower, int upper) {
        
        int rowsize = matrix[0].size();
        
        cout << "lower" << lower << endl;
        cout << "upper" << upper << endl;
        
        if (lower == upper) {
            return searchInRow(matrix[lower], target, 0, matrix[lower].size() - 1);
        }
        
        int middle = (upper + lower) / 2;
        
        cout << middle << endl << endl;
        
        if (matrix[middle][rowsize-1] < target) {
            return searchForRow(matrix, target, middle+1, upper);
        }
        else {
            return searchForRow(matrix, target, lower, middle);
        }
        
        return false;
    }
    
    bool searchInRow(vector<int>& v, int target, int l, int r) {
        
        if (l == r && v[l] != target) return false;
        
        int middle = (l + r) / 2;
        
        cout << middle << endl;
        cout << v[middle] << endl << endl;
        if (v[middle] == target) {
            return true;
        }
        else if (v[middle] > target) {
            return searchInRow(v, target, l, middle);
        }
        else {
            return searchInRow(v, target, middle+1, r);
        }
        
    }
    
};