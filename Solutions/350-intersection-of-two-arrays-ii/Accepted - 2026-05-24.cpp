#include <map>
#include <vector>
#include <cmath>

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        map<int, int> mapa1;
        map<int, int> mapa2;
        map<int, int>::iterator it;
        map<int, int>::iterator current;
        vector<int> out;
        int i;
        for (i = 0; i < nums1.size(); i++){
            it = mapa1.find(nums1[i]);
            if (it == mapa1.end()){
                mapa1.insert({nums1[i], 1});
            } else {
                it->second++;
            }
        }
        for (i = 0; i < nums2.size(); i++){
            it = mapa2.find(nums2[i]);
            if (it == mapa2.end()){
                mapa2.insert({nums2[i], 1});
            } else {
                it->second++;
            }
        }
        for(current = mapa2.begin(); current != mapa2.end(); current++){
            it = mapa1.find(current->first);
            if (it == mapa1.end()) continue;
            for(i = 0; i < min(it->second, current->second); i++){
                out.push_back(it->first);
            }
        }
        return out;
    }
};