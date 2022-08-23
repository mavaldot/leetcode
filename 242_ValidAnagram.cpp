#include <iostream>
#include <vector>
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        
        int size1 = s.size();
        int size2 = t.size();
        
        if (size1 != size2) return false;
        
        for (int i = 0; i < size1; i++) {
            size_t pos = t.find(s[i]);
            if (pos == string::npos) return false;
            t.erase(t.begin() + pos);
        }
        
        if (t == "") return true;
        else return false;
        
    }
};