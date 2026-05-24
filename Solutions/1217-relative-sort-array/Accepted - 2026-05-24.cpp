#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        vector<int> v(1001, 0);
        vector<int> out;
        vector<int>::iterator it;
        for(it = arr1.begin(); it != arr1.end(); it++){
            v[*it] ++;
        }
        for(it = arr2.begin(); it != arr2.end(); it++){ 
            while(v[*it]){
                out.push_back(*it);
                v[*it]--;
            }
        }
        for(int i = 0; i < v.size(); i++){
            while(v[i] > 0){
                out.push_back(i);
                v[i]--;
            }
        }      
        return out;
    }
};