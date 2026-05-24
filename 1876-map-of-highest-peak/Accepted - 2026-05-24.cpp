#include <limits>
#include <queue>

using namespace std;

class Solution {
public:
    const int dx[4] = {-1, 1, 0, 0};
    const int dy[4] = {0, 0, -1, 1};
    bool isValid(int x, int y, int N, int M, vector<vector<bool>>& visited) {
        return y >= 0 && y < N && x >= 0 && x < M && !visited[y][x];
    }

    void bfs(vector<vector<int>>& island, int N, int M, int y, int x){
        island[y][x] = 0;
        queue<pair<int, int>> q;
        vector<vector<bool>> visited(N, vector<bool>(M, false));
        q.push({y, x});
        visited[y][x] = true;
        while(!q.empty()){
            auto [y, x] = q.front();
            q.pop();
            for (int i = 0; i < 4; ++i) {
                int X = x + dx[i];
                int Y = y + dy[i];

                if (isValid(X, Y, N, M, visited)) {
                    visited[Y][X] = true;
                    island[Y][X] = min(island[y][x] + 1, island[Y][X]);
                    q.push({Y, X});
                }
            }
        }
    }
    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
        int N = isWater.size();
        int M = isWater[0].size();
        const int MAX_INT = numeric_limits<int>::max(); 
        vector<vector<int>> island(N, vector<int>(M, MAX_INT));
        for(int i = 0; i < N; i++){
            for(int j = 0; j < M; j++){
                if(isWater[i][j] == 1){
                    bfs(island, N, M, i, j);
                }
            }
        }


        return island;
    }
};