class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int left = 0, right = nums.size();
        int lborder = 0, rborder = nums.size() - 1;
        int m, index_found = -1;
        vector<int> out(2, -1);
        bool flag = false;
        while (left < right){
            m = (left + right) / 2;
            if (nums[m] == target){
                out[0] = m;
                out[1] = m;
                flag = true;
                break;
            } 
            if (nums[m] < target) left = m + 1;
            else right = m - 1;
        }
        if (flag){
            while (out[0] != lborder){
                if (nums[out[0] - 1] == nums[out[0]]) out[0]--;
                else break;
            }
            while (out[1] != rborder){
                if (nums[out[1] + 1] == nums[out[1]]) out[1]++;
                else break;
            }
        }
        return out;
    }
};