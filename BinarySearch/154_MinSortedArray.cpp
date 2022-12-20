#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        while (left < right) {
            std::cout << "Right: " << right << std::endl;
            std::cout << "Left: " << left << std::endl;
            int mid = (right + left) / 2;
            std::cout << "Mid: " << mid << std::endl << std::endl;

            if (mid == left) {
                if (nums[mid] < nums[right]) {
                    return nums[mid];
                }
                else {
                    return nums[right];
                }
            }

            if (nums[left] > nums[right]) {
                if (nums[mid] < nums[left]) {
                    right = mid;
                }
                else {
                    left = mid;
                }
            }
            else if (nums[right] > nums[left]) {
                right = mid;
            }
        }

        return nums[left];
    }
};
