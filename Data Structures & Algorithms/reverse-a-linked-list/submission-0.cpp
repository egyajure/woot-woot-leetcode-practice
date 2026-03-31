/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (!head) return nullptr;
        if(!head->next) return head; // could combine with an or?
        ListNode* temp = reverseList(head->next); // traverse first
        head->next->next = head;
        head->next = nullptr; //!! we dont want any forward links
        return temp;
    }
};
