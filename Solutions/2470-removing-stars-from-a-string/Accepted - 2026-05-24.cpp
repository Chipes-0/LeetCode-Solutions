#include <stack>
#include <string>

using namespace std;

class Solution {
public:
    string removeStars(string s) {
        stack<char> stack;
        string out;

        for(char c : s){
            if (c == '*'){
                stack.pop();
            } else {
                stack.push(c);
            }
        }
        while(!stack.empty()){
            out = stack.top() + out;
            stack.pop();
        }
        return out;
    }
};