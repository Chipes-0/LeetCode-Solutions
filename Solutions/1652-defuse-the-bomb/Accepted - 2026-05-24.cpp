class Solution {
public:
    vector<int> decrypt(vector<int>& code, int k) {
        int n = code.size();
        vector<int> out(n, 0);
        if (!k) return out;

        int start = 1, end = k, sum = 0;
        if(k < 0){
            start = n + k;
            end = n - 1;
        }
        for(int i = start; i <= end; i++){
            sum += code[i];
        }
        for(int i = 0; i < n; i++){
            out[i] = sum;
            cout << sum << "\n";
            sum -= code[start];
            start = (start + 1) % n;
            end = (end + 1) % n;
            sum += code[end];
        }
        return out;
    }
};