class Solution {
public:
    int maximumSwap(int num) {
        string s_num = to_string(num);
        int last_index[10] = {-1, -1, -1, -1, -1, -1, -1, -1, -1, -1};
        for (int i = 0; i < s_num.length(); i++){
            last_index[s_num[i] - '0'] = i;
        }
        char temp;
        for(int i = 0; i < s_num.length(); i++){
            for(int j = 9; j > s_num[i] - '0'; j--){
                if (i < last_index[j]){
                    swap(s_num[i], s_num[last_index[j]]);
                    return stoi(s_num);
                }
            }
        }
        return num;
    }
};