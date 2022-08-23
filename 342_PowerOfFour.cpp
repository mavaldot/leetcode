

#include <cmath>

class Solution {
public:
    bool isPowerOfFour(int n) {
        int i = 0;
        for (;;) {
            long num = pow(4, i);
            if (n == num) return true;
            if (num > n) return false;
            i++;
        }
    }
};