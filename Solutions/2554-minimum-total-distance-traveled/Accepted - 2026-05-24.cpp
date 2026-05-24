#include <limits>
#include <algorithm>
#include <cmath>

class Solution {
public:
    long long minimumTotalDistance(vector<int>& robot, vector<vector<int>>& factory) {
        reverse(robot.begin(), robot.end());
        vector<int> factory_unpack;
        for(vector<int> a: factory){
            for(int i = 0; i < a[1]; i++){
                factory_unpack.push_back(a[0]);
            }
        }
        int r_size = robot.size();
        int f_size = factory_unpack.size();
        sort(factory_unpack.begin(), factory_unpack.end());
        sort(robot.begin(), robot.end());

        vector<vector<long long>> dp(r_size + 1, vector<long long>(f_size + 1, 0));
        for(int i = 0; i < r_size; i++){
            dp[i][f_size] = 1e10;
        }

        long long skip, take;
        for(int i = r_size -1; i >= 0; i--){
            for(int j = f_size -1; j >= 0; j--){
                skip = dp[i][j+1];
                take = abs(factory_unpack[j] - robot[i]) + dp[i+1][j+1];
                dp[i][j] = min(skip, take);
            }
        }

        return dp[0][0];
    }
};