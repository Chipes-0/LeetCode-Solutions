#define oo 2            
// infinite
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<double> D;          // Array of distances
    vector<int> V;             // Array of visited nodes
    vector<vector<double>> W;  // Adjacency matrix

    int minvertex(int n){
        double minVal = oo;
        int pos = -1;
        for (int i = 0; i < n; i++) {
            if (V[i] == 0 && D[i] < minVal) {
            minVal = D[i];
            pos = i;
            }
        }  
        return pos;
    }

    void dijkstra(int start, int n){
        D[start] = 1;
        int pos;
        for (int i = 0; i < n; i++){
            pos = minvertex(n);
            if (pos == -1) break;
            V[pos] = 1;
            for (int j = 0; j < n; j++){
                if (V[j] == 0){
                    D[j] = -min(D[j], D[pos] * W[pos][j]);
                }
            }
            for(int a = 0; a < n; a++){
                cout << D[a] << " ";
            }
            cout << "\n";
            for(int a = 0; a < n; a++){
                cout << V[a] << " ";
            }
            cout << "\n";
        }
    }


    double maxProbability(int n, vector<vector<int>>& edges, vector<double>& succProb, int start_node, int end_node) {
        int m = edges.size();   // edges

        // initialize adjacency matrix, distances, and visited
        W = vector<vector<double>>(n, vector<double>(n, oo));
        V = vector<int>(n, 0);
        D = vector<double>(n, 1);

        for(int i = 0; i < n; i++){
            D[i] = oo;
        }
        for(int i = 0; i < m; i++){
            W[edges[i][0]][edges[i][1]] = succProb[i];
            W[edges[i][1]][edges[i][0]] = succProb[i];
        }
        dijkstra(start_node, n);
        if(abs(D[end_node]) == 2) return 0;
        return D[end_node];
    }
};