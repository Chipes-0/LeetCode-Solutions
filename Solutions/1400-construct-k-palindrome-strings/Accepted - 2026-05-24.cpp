class Solution {
public:
    bool canConstruct(string s, int k) {
        vector<int> freq(26, 0);
        if (s.length() < k) return false;
        for(char c: s){
            freq[c - 'a']++;
        }
        for(int i = 0; i < 26; i++){
            if(freq[i] & 1) k--;
            if(k == -1) return false;
        }
        return true;
    }
};