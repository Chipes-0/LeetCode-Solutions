#include <iostream>
#include <algorithm>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int current = 0;
        int temp;
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == 0){
                swap(nums[current], nums[i]);
                current++;
            }
        }
        for(int i = current; i < nums.size(); i++){
            if(nums[i] == 1){
                swap(nums[current], nums[i]);
                current++;
            }
        }
        for(int i = current; i < nums.size(); i++){
            if(nums[i] == 2){
                swap(nums[current], nums[i]);
                current++;
            }
        }
    }
};