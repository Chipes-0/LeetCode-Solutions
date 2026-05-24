#include <queue>

class Solution {
public:
    int minOperations(vector<string>& logs) {
        queue<int> q;
        int out = 0;
        for(int i = 0; i < logs.size(); i++){
            if (logs[i].compare("../") == 0){
                if (out > 0)
                    out --;
            } else if (logs[i].compare("./") == 0){
                
            }
            else{
                out ++;
            }
        }  
        return out;
    }
};