class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        stack<int> ms;
        int latest_chunk;
        for(int n : arr){
            if(ms.empty()) ms.push(n);
            else if (n > ms.top()){
                ms.push(n);
            } else {
                latest_chunk = ms.top();
                while(!ms.empty() && n < ms.top()) ms.pop();
                ms.push(latest_chunk);
            }
        }
        return ms.size();
    }
};