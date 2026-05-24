#include <bitset>
#include <queue>

using namespace std;

class Solution {
public:
    bool canChange(string start, string target) {
        int N = target.length();

        queue<pair<char, int>> targetS;
        queue<pair<char, int>> startS;

        for (int i = 0; i < N; i++){
            if (start[i] != '_'){
                startS.push(make_pair(i, start[i]));
            }
            if (target[i] != '_'){
                targetS.push(make_pair(i, target[i]));
            }
        }  
        if (targetS.size() != startS.size()) return false;
        pair<int, char> v1;
        pair<int, char> v2;
        while(!targetS.empty()){
            v1 = startS.front();
            v2 = targetS.front();          
            startS.pop();
            targetS.pop();
            if(v1.second != v2.second) return false;
            if(v1.second == 'L' && v1.first < v2.first) return false;
            if(v1.second == 'R' && v1.first > v2.first) return false;
        }
        return true;
    }
};