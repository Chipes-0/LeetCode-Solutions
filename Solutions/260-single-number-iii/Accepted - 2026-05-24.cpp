class Solution {
public:
    vector<int> singleNumber(vector<int>& nums) {
        int xor_0 = 0;
        vector<int> out;
        for(int n : nums){
            xor_0 ^= n;
        }
        int bits = 0;
        while(((xor_0 >> bits) & 1) == 0){
            bits++;
        }
        int xor_1 = 0;
        int xor_2 = 0;
        for(int num : nums){
            if(((num >> bits) & 1) == 1){
                xor_1 ^= num;
            } else {
                xor_2 ^= num;
            }
        }
        out.push_back(xor_1);
        out.push_back(xor_2);
        return out;
    }
};