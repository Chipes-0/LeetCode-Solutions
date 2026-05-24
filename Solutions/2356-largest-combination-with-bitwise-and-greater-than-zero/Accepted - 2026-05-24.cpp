class Solution {
public:
    int largestCombination(vector<int>& candidates) {
        vector<int> bits(24, 0);
        for(int n: candidates){
            for(int i = 0; i < 24; i++){
                bits[i] += n & 1;
                n = n >> 1;
            }
        }
        int out = 0;
        for(int i = 0; i < 24; i++){
            if(bits[i] > out){
                out = bits[i];
            }
        }
        return out;
    }
};