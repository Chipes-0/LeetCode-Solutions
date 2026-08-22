class Solution {
public:
    int findTheWinner(int n, int k) {
        vector<int> v(n, 0);
        for(int i = 1; i <= n; i++){
            v[i - 1] = i;
        }
        int index = 0;
        int remove;
        while (v.size() != 1){
            remove = (index + k - 1) % v.size();
            v.erase(v.begin() + remove);
            index = remove;
        }
        return v[0];

    }
};