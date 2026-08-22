class Solution {
public:
    long long maximumTripletValue(vector<int>& nums) {
        int n = nums.size();
        vector<int> prefix = vector(n + 1, 0);
        vector<int> suffix = vector(n + 1, 0);

        for(int i = 0; i < n; i++){
            if (nums[i] > prefix[i]){
                prefix[i + 1] = nums[i];
            } else{
                prefix[i + 1] = prefix[i];
            }

            if(nums[n - 1 - i] > suffix[i]){
                suffix[i + 1] = nums[n - 1 - i];
            } else {
                suffix[i + 1] = suffix[i];
            }
        }
        long long max_val = 0;
        long long val;
        for (int i = 0; i < n; i++){
            val = long(prefix[i] - nums[i]) * suffix[i];
            max_val = val > max_val ? val : max_val;
        }
        return max_val;
    }
};