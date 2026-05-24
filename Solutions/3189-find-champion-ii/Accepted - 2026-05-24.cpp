class Solution {
public:
    int findChampion(int n, vector<vector<int>>& edges) {
        vector<int> inputs(n, 0);
        vector<int> outputs(n, 0);

        for(auto& e: edges){
            outputs[e[0]]++;
            inputs[e[1]]++;
        }

        int out = -1;
        for(int i = 0; i < n; i++){
            if(outputs[i] == 0 && inputs[i] == 0) return -1;
            if(outputs[i] > 0 && inputs[i] == 0){
                if(out != -1) return -1;
                out = i;
            }
        }
        return out;
    }
};