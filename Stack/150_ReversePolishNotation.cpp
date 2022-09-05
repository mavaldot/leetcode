#include <vector>
#include <stack>
#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<string> stk;
        
        for (auto& c : tokens) {
            cout << c;
            if (c == "+") {
                int o1 = stoi(stk.top());
                stk.pop();
                int o2 = stoi(stk.top());
                stk.pop();
                stk.push(to_string(o1+o2));
            }
            else if (c == "-") {
                int o1 = stoi(stk.top());
                stk.pop();
                int o2 = stoi(stk.top());
                stk.pop();
                stk.push(to_string(o2 - o1));
            }
            else if (c == "*") {
                int o1 = stoi(stk.top());
                stk.pop();
                cout << stk.top();
                int o2 = stoi(stk.top());
                cout << o2;
                stk.pop();
                stk.push(to_string(o1 * o2));
            }
            else if (c == "/") {
                int o1 = stoi(stk.top());
                stk.pop();
                int o2 = stoi(stk.top());
                stk.pop();
                stk.push(to_string(o2 / o1));
                cout << stk.top();
            }
            else {
                stk.push(c);
            }
        }
        
        string s = stk.top();
        int res = stoi(s);
        
        return res;
    }
};