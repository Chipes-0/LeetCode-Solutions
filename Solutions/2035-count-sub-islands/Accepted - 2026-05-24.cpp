class Solution {
public:
    void deleteisland(vector<vector<int>>& grid, int i, int j){
        if (grid[i][j] == 0) return;
        grid[i][j] = 0;
        if (i - 1 >= 0){
            deleteisland(grid, i - 1, j);
        }
        if (j - 1 >= 0){
            deleteisland(grid, i, j - 1);
        }
        if (i + 1 < grid.size()){
            deleteisland(grid, i + 1, j);
        }
        if (j + 1 < grid[0].size()){
            deleteisland(grid, i, j + 1);
        }
    }
    int countSubIslands(vector<vector<int>>& grid1, vector<vector<int>>& grid2) {
        int n = grid1.size();
        int m = grid1[0].size();
        for(int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (grid2[i][j] == 1 && grid1[i][j] == 0){
                    deleteisland(grid2, i, j);
                }
            }
        }
        int out = 0;
        for(int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if (grid2[i][j] == 1) {
                    deleteisland(grid2, i, j);
                    out++;
                }
            }          
        }
        return out;
    }
};