#include <queue>

using namespace std;

class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        vector<vector<int>> heap(n, vector<int>(2, 0));
        vector<int> mapeo(n, 0);
        long long out = 0;
        for(int i = 0; i < n; i++){
            heap[i][1] = i;
        } 
        for(vector<int> v: roads){
            heap[v[0]][0]++;
            heap[v[1]][0]++;
        }
        priority_queue<pair<int, int> > pq;
        for (auto p: heap){
            pq.push(make_pair(p[0], p[1]));
        }
        pair<int, int> p;
        int prio = n;
        while(!pq.empty()){
            p = pq.top();
            pq.pop();
            mapeo[get<1>(p)] = prio;
            prio--;
        }
        for(auto r : roads){
            out += mapeo[r[0]] + mapeo[r[1]];
        }
        return out;
    }
};