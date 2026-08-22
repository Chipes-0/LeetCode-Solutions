class Solution {
public:

    void markguarded(int row, int col, vector<vector<int>>& matrix){
        // right
        for(int i = 1; i <= 4; i++){
            if (col + i >= matrix[row].size()){
                break;
            }
            if (matrix[row][col + i] == 2 || matrix[row][col + i] == 1){
                break;
            }
            matrix[row][col + i] = -1;
        }
        // left
        for(int i = 1; i <= 4; i++){
            if (col - i < 0){
                break;
            }
            if (matrix[row][col - i] == 2 || matrix[row][col - i] == 1){
                break;
            }
            matrix[row][col - i] = -1;
        }

        // down
        for(int i = 1; i <= 4; i++){
            if (row + i >= matrix.size()){
                break;
            }
            if (matrix[row + i][col] == 2 || matrix[row + i][col] == 1){
                break;
            }
            matrix[row + i][col] = -1;
        }

        // up
        for(int i = 1; i <= 4; i++){
            if (row - i < 0){
                break;
            }
            if (matrix[row - i][col] == 2 || matrix[row - i][col] == 1){
                break;
            }
            matrix[row - i][col] = -1;
        }
    }

    int countUnguarded(int m, int n, vector<vector<int>>& guards, vector<vector<int>>& walls) {
        int out = 0;
        vector<vector<int>> matrix(m, vector(n, 0));
        for(auto g: guards){
            matrix[g[0]][g[1]] = 1;
        }
        for(auto w: walls){
            matrix[w[0]][w[1]] = 2;
        }

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if (matrix[i][j] == 1){
                    markguarded(i, j, matrix);
                }
            }
        }
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                if(matrix[i][j] == 0) out ++;
            }
        }
        return out;
    }
};