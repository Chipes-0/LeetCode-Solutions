#include <algorithm>

class Solution {
public:
    int maxEqualRowsAfterFlips(vector<vector<int>>& matrix) {
        vector<vector<int>> matrix2(matrix.size(), vector<int>(matrix[0].size()));
        unordered_map<string, int> bitrow;

        for(int row = 0; row < matrix.size(); row++){
            string pattern = "";
            for(int col = 0; col < matrix[row].size(); col++){
                if(matrix[row][col] == matrix[row][0]){
                    pattern += "A";
                } else {
                    pattern += "B";
                }
            }
            bitrow[pattern]++;
        }
        int out = 0;
        for(auto frecuency : bitrow){
            out = max(frecuency.second, out);
        }
        return out;
    }
};