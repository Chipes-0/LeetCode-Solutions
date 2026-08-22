class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& box) {
        int m = box.size(), n = box[0].size();
        vector<vector<char>> rotated_box(n, vector<char>(m, '.'));
        int y;
        for(int i = m - 1; i >= 0; i--){
            for(int j = n - 1; j >= 0; j--){
                if(box[i][j] == '#'){
                    y = j;
                    while(y != n - 1){
                        if(box[i][y + 1] == '*' || box[i][y + 1] == '#'){
                            break;
                        }
                        swap(box[i][y + 1], box[i][y]);
                        y++;
                    }
                }
            }
        }
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                rotated_box[j][m -1 -i] = box[i][j];
            }
        }
        return rotated_box;
    }
};