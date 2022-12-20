#include <vector>
#include <stack>
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) {
        stack<pair<int, int>> stk;
        
        vector<int> res(temperatures.size(), 0);
        
        for (int i = 0; i < temperatures.size(); i++) {
            
            while (!stk.empty()) {
                auto pair = stk.top();
                if (pair.first < temperatures[i]) {
                    res[pair.second] = i - pair.second;
                    stk.pop();
                }
                else break;
            }
            
            stk.push(make_pair(temperatures[i], i));
        }
        
        return res;
    }
};