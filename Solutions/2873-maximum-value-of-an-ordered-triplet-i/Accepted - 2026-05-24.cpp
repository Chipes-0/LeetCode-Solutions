class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        long long max_val = 0;
        long long val;
        int N = nums.size();
        for (int i = 0; i < N; i++){
            for(int j = i + 1; j < N; j++){
                for(int k = j + 1; k < N; k++){
                    val = (nums[i] - nums[j]) * nums[k];
                    if (val > max_val) {
                        max_val = val;
                    }
                }
            }
        }
        return max_val;
    }
};