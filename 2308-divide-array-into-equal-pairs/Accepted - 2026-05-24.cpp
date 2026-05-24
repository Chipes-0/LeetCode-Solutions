class Solution {
public:
    bool divideArray(vector<int>& nums) {
        vector<int> count(500, 0);
        for(auto n : nums){
            count[n - 1]++;
        } 

        for(int i = 0; i < 500; i++){
            if(count[i] & 1) return false;
        }
        return true;
    }
};