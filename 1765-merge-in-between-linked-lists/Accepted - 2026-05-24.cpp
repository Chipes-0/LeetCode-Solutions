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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* list1curr = list1;
        ListNode* head = list1curr;
        ListNode* curr = head;

        for(int i = 0; i < a - 1; i++){
            curr = curr -> next;
            list1curr = list1curr -> next;
        }
        curr -> next = list2;
        for(int i = 0; i < (b - a) + 1; i++){
            list1curr = list1curr -> next;
        }
        while(curr -> next != nullptr){
            curr = curr -> next;
        }
        cout << curr -> val << "\n";
        
        curr -> next = list1curr;

        return head;
    }
};