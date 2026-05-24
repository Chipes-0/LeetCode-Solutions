#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    int getLucky(string s, int k) {
        string total = "";
        for(int i = 0; i < s.size(); i++){
            total += to_string(s[i] - 'a' + 1);
        }
        int out;
        while(k--){
            out = 0;
            for(int i = 0; i < total.size(); i++){
                out += total[i] - '0';
            }
            total = to_string(out);
        }
        return out;
    }
};