#include <queue>

using namespace std;

struct element{
    int prio;
    char var;

    bool operator<(const element& other) const {
        return prio < other.prio;
    }
};

class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        priority_queue<element> pq;
        if(a){
            pq.push({a, 'a'});
        }
        if(b){
            pq.push({b, 'b'});
        }
        if(c){
            pq.push({c, 'c'});
        }

        element first;
        element second;
        string out = "";
        while(!pq.empty()){
            first = pq.top();
            pq.pop();
            if(out.length() >= 2 && out[out.length() - 1] == first.var && out[out.length() - 2] == first.var){
                if (pq.empty()) break;
                second = pq.top();
                pq.pop();
                out += second.var;
                if (second.prio -1 > 0){
                    pq.push({second.prio - 1, second.var});
                }
            }
            out += first.var;
            if (first.prio -1 > 0){
                pq.push({first.prio - 1, first.var});
            }
        }
        return out;
    }
};