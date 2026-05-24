class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int count = 0;
        vector<int>::iterator it;
        for (it = arr.begin(); it != arr.end(); it++){
            if (*it % 2) count += 1;
            else count = 0;

            if (count == 3) return true; 
        }
        return false;
    }
};