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
    ListNode* deleteMiddle(ListNode* head) {
        ListNode* fast = head;
        ListNode* slow = head;
        ListNode* prev = nullptr;
        while(fast->next != nullptr){
            if(slow->next != nullptr){
                prev = slow;
                slow = slow->next;
            } else {
                break;
            }
            if(fast->next != nullptr){
                fast = fast->next;
            } else{
                break;
            }
            if(fast->next != nullptr){
                fast = fast->next;
            } else{
                break;
            }
        }
        prev->next = slow->next;
        return head;
    }
};