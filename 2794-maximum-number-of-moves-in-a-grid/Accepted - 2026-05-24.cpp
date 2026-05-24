#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

class Solution {
public:
    int maxMoves(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        
        // Recorrer la matriz desde la última fila y columna hacia la primera
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                
                // Movimiento diagonal hacia arriba a la izquierda
                if (i - 1 >= 0 && j - 1 >= 0 && grid[i - 1][j - 1] < grid[i][j]) {
                    dp[i - 1][j - 1] = max(dp[i - 1][j - 1], dp[i][j] + 1);
                }
                
                // Movimiento a la izquierda
                if (j - 1 >= 0 && grid[i][j - 1] < grid[i][j]) {
                    dp[i][j - 1] = max(dp[i][j - 1], dp[i][j] + 1);
                }
                
                // Movimiento diagonal hacia abajo a la izquierda
                if (i + 1 < m && j - 1 >= 0 && grid[i + 1][j - 1] < grid[i][j]) {
                    dp[i + 1][j - 1] = max(dp[i + 1][j - 1], dp[i][j] + 1);
                }
            }
        }

        // Imprimir la primera columna de dp para verificar el resultado
        int out = 0;
        for (int i = 0; i < m; i++) {
           out = max(dp[i][0], out);
        }
        
        return out;
    }
};
