class Solution {
public:
    string repeatLimitedString(string s, int repeatLimit) {
        vector<int> v(26, 0);
        for(int i = 0; i < s.length(); i++){
            v[s[i] - 'a']++;
        }
        string out = "";
        int count = 0, prev = -1;
        int j;
        for(int i = 25; i >= 0;){
            if(v[i] == 0){
                i--;
                count = 0;
            } else {
                if (prev == i && count == repeatLimit){
                    j = i - 1;
                    while(j >= 0 && v[j] == 0) j--;
                    if (j < 0) break;
                    out += 'a' + j;
                    v[j]--;
                    count = 1;
                    prev = j;
                } else {
                    out += 'a' + i;
                    prev = i;
                    count++;
                    v[i]--;
                }
            }
        }
        return out;
    }
};