class Solution {
public:
    int appendCharacters(string s, string t) {
        int t_place = 0;
        for (int i = 0; i < s.size(); i++){
            if (t_place == t.size()) break;
            if (s[i] == t[t_place]){
                t_place ++;
            }
        }
        return t.size() - t_place;
    }
};