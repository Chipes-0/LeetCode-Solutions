class Solution {
public:
    bool isArraySpecial(vector<int>& nums) {
        bool* last = nullptr; 
        bool current;
        for(int n : nums){
            if(last == nullptr){
                last = new bool(n & 1);
                continue;
            }
            current = n & 1;
            if (current == *last) return false;
            *last = current;
        }
        return true;
    }
};