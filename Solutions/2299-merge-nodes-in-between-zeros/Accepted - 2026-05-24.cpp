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
    ListNode* mergeNodes(ListNode* head) {
        ListNode* l = head;
        ListNode* r = head;
        int sum = 0;
        while(r){
            sum += r->val;
            if(r->val == 0 && sum > 0){
                r->val = sum;
                l->next = r;
                l = r;
                sum = 0;
            }
            r = r->next;
        }
        return head->next;
    }
};