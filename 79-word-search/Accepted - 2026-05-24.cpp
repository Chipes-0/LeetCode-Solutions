#include <iostream>
#include <algorithm>

class Solution {
public:
    bool dfs(vector<vector<char>>& board, string word, int index, int i, int j){
        if(index == word.length()) return true;
        board[i][j] = '*';
        int up;
        int down;
        int left;
        int right;
        up = std::max(0,i-1);
        down = std::min(int(board.size() -1), i+1);
        right = std::min(int(board.size() -1), j+1);
        left = std::max(0,j-1);
        if (board[up][j] == word[index]){
            if(dfs(board, word, index + 1, i-1, j)) return true;
        }
        if (board[down][j] == word[index]){
            if(dfs(board, word, index + 1, i+1, j)) return true;
        }
        if (board[i][left] == word[index]){
            if(dfs(board, word, index + 1, i, j-1)) return true;
        }
        if (board[i][right] == word[index]){
            if(dfs(board, word, index + 1, i, j + 1)) return true;
        }
        board[i][j] = word[index];
        return false;
    }


    bool exist(vector<vector<char>>& board, string word) {
        for(int i = 0; i < board.size(); i++){
            for(int j = 0; j < board[i].size(); j++){
                if(board[i][j] == word[0]){
                    if(dfs(board, word, 1, i, j)) return true;
                }
            }
        }
        return false;
    }
};