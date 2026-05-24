class StockSpanner {
public:
    stack<pair<int, int>> s;
    StockSpanner() {
        s = stack<pair<int, int>>();
    }
    
    int next(int price) {
        int out = 1;
        while(!s.empty() && s.top().first <= price){
            out += s.top().second;
            s.pop();
        }
        s.push({price, out});
        return out;
    }
};

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner* obj = new StockSpanner();
 * int param_1 = obj->next(price);
 */