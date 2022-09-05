#include <string>
#include <vector>

using namespace std;


class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        
        vector<int> v(26);
        
        for (auto& c : s1) {
            v[c - 'a']++;
        }
        
        for (int i = 0; i < s2.size(); i++) {
            
            vector<int> copy = v;
            bool found = true;
            
            if (s2.size() - i < s1.size()) {
                return false;
            }
            
            for (int j = i; j < s1.size() + i; j++) {
                
                if (copy[s2[j]-'a'] > 0) copy[s2[j]-'a']--;
                else found = false;
            }
            
            if (found) return true;
            
        }
        
        return false;
        
    }
    
};