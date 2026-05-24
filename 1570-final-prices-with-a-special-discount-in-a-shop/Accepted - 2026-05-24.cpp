#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        stack<pair<int, int>> ms;
        pair<int, int> last;
        for(int i = 0; i < prices.size(); i++){
            if(ms.empty()){
                ms.push(make_pair(i, prices[i]));
            } else{
                last = ms.top();
                while(!ms.empty() && last.second >= prices[i]){
                    last = ms.top();
                    prices[last.first] -= prices[i];
                    ms.pop();
                }
                ms.push(make_pair(i, prices[i]));
                
            }
        }
        return prices;
    }
};