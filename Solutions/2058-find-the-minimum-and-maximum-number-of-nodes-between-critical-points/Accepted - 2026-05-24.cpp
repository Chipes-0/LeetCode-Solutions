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
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        vector<int> critical;
        vector<int> out(2, -1);
        ListNode* c = head;
        int prev = 0;
        int index = 0;

        while(c != nullptr){
            if (!prev) {
                prev = c->val;
                c = c->next;
                index++;
            }
            if (c->val > prev){
                if (c->next != nullptr && c->next->val < c->val){
                    critical.push_back(index);
                }
            }
            if (c->val < prev){
                if (c->next != nullptr && c->next->val > c->val){
                    critical.push_back(index);
                }
            }
            prev = c->val;
            c = c->next;
            index++;
        }
        if(critical.size() > 1){
            out[0] = INT_MAX;
            out[1] = critical[critical.size() - 1] - critical[0];
            for(index = 1; index < critical.size(); index++){
                prev = critical[index] - critical[index - 1];
                if (prev < out[0]) out[0] = prev;
            }
        }
        return out;
    }
};