class Solution {
public:
    string countOfAtoms(string formula) {
        string out = "";
        stack<map<string, int>> s;
        map<string, int> topelement;
        map<string, int> prevelement;
        s.push(map<string, int>());

        int i = 0;
        string element;
        int count;
        while (i < formula.length()){
            if (formula[i] == '('){
                s.push(map<string, int>());
            } else if (formula[i] == ')') {
                topelement = s.top();
                s.pop();
                count = 0;
                while(i + 1 < formula.length() && formula[i + 1] >= '1' && formula[i+1] <= '9'){
                    count *= 10;
                    count += formula[i + 1] - '0';
                    i++;
                }
                if(count == 0){
                    count = 1;
                }
                prevelement = s.top();
                for (const auto& pair : topelement) {
                    prevelement[pair.first] += pair.second * count;
                }
                s.top() = prevelement;
            } else {
                element = formula[i];
                count = 0;
                if (i + 1 < formula.length() && formula[i + 1] >= 'a' && formula[i+1] <= 'z'){
                    element += formula[i + 1];
                    i++;
                }
                while(i + 1 < formula.length() && formula[i + 1] >= '1' && formula[i+1] <= '9'){
                    count *= 10;
                    count += formula[i + 1] - '0';
                    i++;
                }
                if(count == 0){
                    count = 1;
                }
                topelement = s.top();
                topelement.insert({element, count});
                s.top() = topelement;

            }
            i++;
        }
        for (const auto& pair : s.top()) {
            out += pair.first;
            if (pair.second != 1){
                out +=  to_string(pair.second);
            }
        }   
        return out;
    }
};