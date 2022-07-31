#include <vector>

using namespace std;
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};

class Solution {
public:
    vector<int> preorder(Node* root) {
        vector<int> vals = {};
        
        if (root == nullptr) return vals;
        
        vals.push_back(root->val);
        if (!root->children.empty()) {
            for (auto& child : root->children) {
            vector<int> results = preorder(child);
            vals.insert(vals.end(), results.begin(), results.end());
            }
        }

        return vals;
    }
};