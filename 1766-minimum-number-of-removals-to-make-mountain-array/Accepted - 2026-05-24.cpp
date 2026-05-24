class Solution {
public:
    int minimumMountainRemovals(vector<int>& nums) {
        int N = nums.size();
        vector<int> LIS(N, 1);
        vector<int> LDS(N, 1);

        for(int i = 1; i < N; i++){
            for(int j = 0; j < i; j++){
                if(nums[i] > nums[j]){
                    LIS[i] = max(LIS[j] + 1, LIS[i]);
                }
            }
        }
        for(int i = 0; i < N; i++){
            for (int j = i; j < N; j++) {
                for (int k = j + 1; k < N; k++) {
                    if (nums[j] > nums[k]) {
                        LDS[j] = max(LDS[j], LDS[k] + 1);
                    }
                }
            }
        }



        int out = N;
        for(int i = 0; i < N; i++){
            out = min(out, N - (LIS[i] + LDS[i] -1));
        }
        return out;

    }
};