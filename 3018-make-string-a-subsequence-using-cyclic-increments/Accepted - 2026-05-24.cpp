class Solution {
public:
    bool canMakeSubsequence(string str1, string str2) {
        int index = 0;
        bool pass = true;
        for(int i = 0; i < str1.length(); i++){
            if(str1[i] == str2[index]){
                index++;
            } else if(str1[i] + 1 == str2[index]){
                index++;
                pass = false;
            } else if(str1[i] == 'z' && str2[index] == 'a'){
                index++;
                pass = false;
            }
        }
        cout << index;
        return index == str2.length();
    }
};