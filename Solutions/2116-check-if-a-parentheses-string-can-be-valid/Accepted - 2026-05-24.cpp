class Solution {
public:
    bool canBeValid(string s, string locked) {
        if (s.length() & 1) return false;
        int open = 0;
        int unlocked = 0;
        for (int i = 0; i < s.length(); i++){
            if (locked[i] == '0'){
                unlocked ++;
            } else if(s[i] == '('){
                open ++;
            } else if(open > 0){
                open --;
            } else if(unlocked > 0){
                unlocked --;
            } else {
                return false;
            }
        }

        open = 0;
        unlocked = 0;
        for (int i = s.length() - 1; i >= 0; i--){
            if (locked[i] == '0'){
                unlocked ++;
            } else if(s[i] == ')'){
                open ++;
            } else if(open > 0){
                open --;
            } else if(unlocked > 0){
                unlocked --;
            } else {
                return false;
            }
        }
    return true;
    }
};