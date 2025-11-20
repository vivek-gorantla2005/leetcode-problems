class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& a, vector<int>& b) {
        unordered_map<int,int>m;
        vector<int>ans;
        for(int i = 0 ; i < a.size();i++){
            m[a[i]]++;
            m[b[i]]++;
            int curr= 0;
            for(auto &[num,cnt] : m){
                if(cnt == 2){
                    curr++;
                }
            }
            ans.push_back(curr);
        }   
        return ans;
    }
};