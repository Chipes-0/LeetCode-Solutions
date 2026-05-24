class Solution {
public:
    void reverseString(vector<char>& s) {
        int left = 0;
        int right = s.size() - 1;
        char aux;
        while (left < right){
            aux = s.at(left);
            s.at(left) = s.at(right);
            s.at(right) = aux;
            left ++;
            right --;
        }
    }
};