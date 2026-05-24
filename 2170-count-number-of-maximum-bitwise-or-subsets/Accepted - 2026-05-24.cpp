class Solution {
public:
    int out = 0;
    void bt(int target, int current, int index, vector<int>& nums){
        if (index == nums.size()){
            if (current == target){
                out++;
            }
            return;
        }

        if(index >= nums.size() || current > target) return;
        bt(target, current | nums[index], index + 1, nums);
        bt(target, current, index + 1, nums);     
    }

    int countMaxOrSubsets(vector<int>& nums) {
        int max_or = 0;
        for(int n: nums){
            max_or |= n;
        }
        bt(max_or, 0, 0, nums);
        return out;
    }
};