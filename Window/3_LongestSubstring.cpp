#include <string>

using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        if (s.size() == 0) return 0;
        
        int longest = 1;
        
        for (int i = 0; i < s.size(); i++) {
            int l = 1;
            for (int j = i + 1; j < s.size(); j++) {
                if (s.substr(i, j-i).find(s[j]) != string::npos) {
                    if (l > longest) longest = l;
                    break;
                }
                else {
                    l++;
                }
            }
            if (l > longest) longest = l;
        }
        
        return longest;
        
    }
};