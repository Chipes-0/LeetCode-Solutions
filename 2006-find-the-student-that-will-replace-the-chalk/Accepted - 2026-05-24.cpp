class Solution {
public:
    int chalkReplacer(vector<int>& chalk, int k) {
        int N = chalk.size();
        int i = 0;
        while(1){
            if (k < chalk[i]) return i;
            k -= chalk[i];
            i = (i + 1) % N; 
        }
        return 0;

        return 0;
    }
};