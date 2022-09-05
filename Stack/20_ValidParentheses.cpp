#include <string>
#include <stack>

using namespace std;

class Solution {

public:
    bool isValid(string s) {
        stack<char> stk;
        
        for (char& c : s) {
            if (c == '(' || c == '{' || c == '[') {
                stk.push(c);
            }
            else {
                if (stk.empty()) {
                    return false;
                }
                else {
                    char top = stk.top();
                    stk.pop();
                    if (top == '(' && c != ')') return false;
                    if (top == '{' && c != '}') return false;
                    if (top == '[' && c != ']') return false;
                }
            }
        }
        
        return stk.empty();
    }
};