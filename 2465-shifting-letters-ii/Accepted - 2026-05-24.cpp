class Solution {
public:
    string shiftingLetters(string s, vector<vector<int>>& shifts) {
        int direction = 0;
        char l;
        for(auto q : shifts){
            if(q[2] == 1) direction = 1;
            else direction = -1;
            for(int i = q[0]; i < q[1] + 1; i++){
               s[i] = 'a' + (s[i] - 'a' + direction + 26) % 26;
            }
        }
        return s;
    }
};