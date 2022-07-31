#include <unordered_map>
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int longestPalindrome(string s) {
    return 0;
}

int greatestSum(vector<int>& v, int n) {
    int greatest = 0;
    int sum = 0;
    int index = 0;
    for (int i = 0; i < v.size() - n + 1; i++) {
        cout << i << ":" << v[i] << endl;
        for (int j = i; j < i + n; j++) {
            sum += v[j];
        }
        if (sum > greatest) {
            greatest = sum;
            index = i;
        }
        sum = 0;
    }
    v.erase(v.begin()+index, v.begin()+index+n);

    return greatest;
}  

int main() {
    vector<int> a = {1, 7, 8, 2, 3, 9};
    vector<int> b = {2, 1};

    sort(b.begin(), b.end(), greater<>());
    int profit = 0;

    for (auto& num : b) {
        profit += greatestSum(a, num);
    }
    cout << endl;
    cout << profit;

}
