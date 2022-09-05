#include <string>
#include <cctype>
#include <cwctype>
#include <iostream>

using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0;
        int r = s.size() - 1;
        
        while (l <= r) {
            if (!iswalnum(s[l])) {
                l++;
                continue;
            }
            if (!iswalnum(s[r])) {
                r--;
                continue;
            }
            if (toupper(s[l]) != toupper(s[r])) {
                cout << l << s[l] << endl;
                cout << r << s[r] << endl;
                return false;
            }
            l++;
            r--;
        }
        
        return true;
    }
};