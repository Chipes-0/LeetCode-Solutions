class Solution {
public:
    int hasprefix(string word, string pref){
        if(pref.length() > word.length()) return 0;
        for(int i = 0; i < pref.length(); i++){
            if(word[i] != pref[i]) return 0;
        }
        return 1;
    }

    int prefixCount(vector<string>& words, string pref) {
        int out = 0;
        for (auto w : words){
            out += hasprefix(w, pref);
        }
        return out;
    }
};