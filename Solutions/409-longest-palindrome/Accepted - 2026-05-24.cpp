#include <map>

class Solution {
public:
    int longestPalindrome(string s) {
        map<char, int> counter;
        map<char, int>::iterator it;
        int out = 0;
        int max_odd = 0;
        for(char c : s){
            it = counter.find(c);
            if(it == counter.end()){
                counter.insert({c, 1});
            }
            it->second = it->second + 1;
        }
        for(it = counter.begin(); it != counter.end(); it++){
            if(it->second % 2 == 0) out += it->second;
            else if (it->second > max_odd){
                max_odd = it->second;
            }
        }
        return out + max_odd;
    }
};