#include <algorithm> 

class Solution {
public:
    int bs(int left, int right, vector<int>& nums, int search){
        int m;
        while (left < right){
            m = (left + right) / 2;
            if (nums[m] == search){
                left = m;
                break;
            } else if (nums[m] > search){
                right = m - 1;
            } else {
                left = m + 1;
            }
        }
        return left;
    }
    int maximumCount(vector<int>& nums) {
        int N = nums.size();
        int zero_index = bs(0, N, nums, 0);
        int l = zero_index;
        int r = zero_index;
        while (l < N && (nums[l] == 0 || nums[l] < 0)){
            l++;
        }
        while (r >= 0 && nums[r] == 0){
            r--;
        }
        return max(r + 1, N -l);
    }
};