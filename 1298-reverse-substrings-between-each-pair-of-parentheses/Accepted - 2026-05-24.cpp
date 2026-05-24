#include <stack>

class Solution {
public:
    string reverseParentheses(string s) {
        stack<int> word_s;
        string out = "";
        vector<int> v(s.length(), -1);
        int i, j;
        for(i = 0; i < s.length(); i++){
            if (s[i] == '(') word_s.push(i);
            if (s[i] == ')'){
                j = word_s.top();
                word_s.pop();
                v[i] = j;
                v[j] = i;
            }
        }
        i = 0;
        int move = 1;
        while(i < s.length()){
            if (s[i] == '(' || s[i] == ')'){
                i = v[i];
                move *= -1;
            } else{
                out += s[i];
            }
            i += move;
        }
        return out;
    }
};