class Solution {
public:
    string reversePrefix(string word, char ch) {
        string out = "";
        bool flag = true;
        for(int i = 0; i < word.size(); i++){
            if(word[i] == ch && flag){
                int j = i;
                while (j >= 0){
                    out += word[j];
                    j--;
                }
                flag = false;
                continue;
            }
            if(!flag){
                out += word[i];
            }
        }
        if(flag) return word;
        return out;
    }
};