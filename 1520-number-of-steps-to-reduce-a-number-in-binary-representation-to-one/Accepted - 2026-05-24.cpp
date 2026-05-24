#include <vector>
using namespace std;

class Solution {
public:
    int numSteps(string s) {
        int out = 0;
        int N = s.size();
        int iterator;
        vector<bool> bits;
        for(int i = 0; i < N; i++){
            bits.push_back(s[N-1-i] == '1');
        }
        while (bits.size() > 1){
            out++;
            if(bits[0] == 0){
                bits.erase(bits.begin());
            }else{
                iterator = 0;
                while(iterator != bits.size()){
                    if(bits[iterator] == 1){
                        bits[iterator] = 0;
                    }else{
                        bits[iterator] = 1;
                        break;
                    }
                    iterator++;
                }
                if(iterator != bits.size()){
                    bits.push_back(1);
                }
            }
        }

        return out;
    }
};