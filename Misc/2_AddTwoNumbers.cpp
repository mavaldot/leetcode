#include <iostream>
#include <vector>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* head = new ListNode(0);
        ListNode* current = nullptr;

        bool flag = true;
        int sum = 0;
        int carry = 0;
        while (flag) {
            int sum = 0;

            if (l1 == nullptr && l2 == nullptr && carry != 1) {
                flag = false;
                break;
            }
            else if (current != nullptr) {
                current->next = new ListNode;
                current = current->next;
            }
            else {
                current = head;
            }

            if (l1 != nullptr) {
                sum += l1->val;
                l1 = l1->next;
            }
            if (l2 != nullptr) {
                sum += l2->val;
                l2 = l2->next;
            }

            sum += carry;
            carry = 0;
            if (sum >= 10) {
                carry = 1;
                sum -= 10;
            }

            current->val = sum;
        }
        
        return head;
}

int main() {

}