class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        double out = 0;
        int time = 0;
        for (int i = 0; i < customers.size(); i++){
            if (time < customers[i][0])
                time = customers[i][0];
            time += customers[i][1];
            out += time - customers[i][0];
        }
        return out / customers.size();
    }
};