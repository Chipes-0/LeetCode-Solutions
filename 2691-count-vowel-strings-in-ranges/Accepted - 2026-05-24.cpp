class Solution {
public:
    vector<int> vowelStrings(vector<string>& words, vector<vector<int>>& queries) {
        string vowels = "aeiou";
        int N = words.size();
        vector<int> transformed(N, 0);
        vector<int> prefixsum(N + 1, 0);

        string w;
        for(int i = 0; i < N; i++){
            w = words[i];
            if(vowels.find(w[0]) != string::npos && vowels.find(w[w.length() - 1]) != string::npos){
                transformed[i] = 1;
            }
        }
        for(int i = 1; i < N + 1; i++){
            prefixsum[i] = prefixsum[i - 1] + transformed[i - 1];
        }
        
        vector<int> out(queries.size(), 0);
        int i = 0;
        for(auto q: queries){
            out[i] = prefixsum[q[1] + 1] - prefixsum[q[0]];
            i++;
        }
        return out;
    }
};