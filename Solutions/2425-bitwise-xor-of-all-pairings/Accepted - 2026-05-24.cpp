class Solution {
public:
    int xorAllNums(vector<int>& nums1, vector<int>& nums2) {
        int n = nums2.size();
        int m = nums1.size();
        int out = 0;
        if(n & 1){
            for(int n1 : nums1){
                out ^= n1;
            }
        }
        if(m & 1){
            for(int n2 : nums2){
                out ^= n2;
            }
        }
        
        return out;
    }
};