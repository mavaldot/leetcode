#include <string>
#include <iostream>
#include <vector>
#include <iterator>
#include <algorithm>

using namespace std;

class Solution {
public:
    int trap(vector<int>& height) {
        
        int top = 0;
        int total = 0;
        
        int max = distance(height.begin(), max_element(height.begin(), height.end()));
        
        for (int i = 0; i < max + 1; i++) {
            if (height[i] == 0) continue;
            
            int acc = 0;
            
            top = height[i];
            for (int j = i + 1; j < max + 1; j++) {
                if (height[j] >= top) {
                    total += acc;
                    acc = 0;
                    i = j - 1;
                    break;
                }
                else {
                    acc += top - height[j];
                }
            }
        }
        
        for (int i = height.size() - 1; i > max - 1; i--) {
            if (height[i] == 0) continue;
            
            int acc = 0;
            
            top = height[i];
            for (int j = i - 1; j > max - 1; j--) {
                if (height[j] >= top) {
                    total += acc;
                    acc = 0;
                    i = j + 1;
                    break;
                }
                else {
                    acc += top - height[j];
                }
            }
        }
        
        
        return total;
        
    }
};