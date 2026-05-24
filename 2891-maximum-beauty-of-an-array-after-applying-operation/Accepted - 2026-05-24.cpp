#include <algorithm>

using namespace std;

class Solution {
public:
    int maximumBeauty(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        // 1 2 4 6
        int out = 1;
        int right = 0;
        for(int left = 0; left < nums.size(); left++){
            while(right < nums.size() && nums[right] - nums[left] <= 2 * k){
                right++;
            }
            out = max(out, right - left);
        }
        return out;
    }
};