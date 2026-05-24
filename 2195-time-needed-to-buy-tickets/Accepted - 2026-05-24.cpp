class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int out = 0;
        while(tickets.at(k) != 0){
            for(int i = 0; i < tickets.size(); i++){
                if(tickets.at(i) > 0){
                    out ++;
                    tickets.at(i) = tickets.at(i) - 1;
                }
            }
        }
        return out;
    }
};