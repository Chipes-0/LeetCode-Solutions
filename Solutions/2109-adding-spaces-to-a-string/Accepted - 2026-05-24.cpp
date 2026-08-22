class Solution {
public:
    string addSpaces(string s, vector<int>& spaces) {
        string out(s.length() + spaces.size(), ' ');
        int index = 0;
        for(int i = 0; i < out.length(); i++){
            if(index < spaces.size() && i-index == spaces[index]){
                index++;
                continue;
            } 
            out[i] = s[i -index];
        }
        return out;
    }
};