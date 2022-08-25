#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        int n = board.size();
        
        for (int i = 0; i < n; i++) {
            vector<char> row;
            for (int j = 0; j < n; j++) {
                char& c = board[i][j];
                if (c == '.') continue;
                if (find(row.begin(), row.end(), c) != row.end()) {
                    return false;
                }
                row.push_back(c);
            }
        }
        
        for (int i = 0; i < n; i++) {
            vector<char> col;
            for (int j = 0; j < n; j++) {
                char& c = board[j][i];
                if (c == '.') continue;
                if (find(col.begin(), col.end(), c) != col.end()) {
                    return false;
                }
                col.push_back(c);
            }
        }
        
        for (int i = 0; i < 9; i+=3) {
            for (int j = 0; j < 9; j+=3) {
                vector<char> square;
                for (int k = i; k < i + 3; k++) {
                    for (int l = j; l < j + 3; l++) {
                        char& c = board[k][l];
                        if (c == '.') continue;
                        if (find(square.begin(), square.end(), c) != square.end()) {
                            return false;
                        }
                        square.push_back(c);
                    }
                }
            }
        }
        
        return true;
        
    }
};