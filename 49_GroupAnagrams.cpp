#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> groups;
        vector<string> word;    
        
        for (string& s : strs) {
            string copy = s;
            vector<string> av = {"a"};
            sort(s.begin(), s.end());
            auto f = find(word.begin(), word.end(), s);
            if (f == word.end()) {
                word.push_back(s);
                groups.push_back({copy});
            }
            else {
                int i = distance(word.begin(), f);
                groups[i].push_back(copy);
            }
        }
        
        return groups;
    }
};