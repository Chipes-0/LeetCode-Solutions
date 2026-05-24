class Solution {
public:
    int minFlips(int a, int b, int c) {
        int out = 0;
        for(int i = 0; i < 32; i++){
            if (!(c & 1)){
                out += (a & 1) + (b & 1);
            } else {
                out += (a & 1) + (b & 1) < 1 ? 1 : 0;
            }
            a = a >> 1;
            b = b >> 1;
            c = c >> 1;
        }
        return out;
    }
};