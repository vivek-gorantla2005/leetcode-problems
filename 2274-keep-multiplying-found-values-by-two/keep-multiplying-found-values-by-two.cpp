class Solution {
public:
    int findFinalValue(vector<int>& nums, int original) {
        unordered_set<int>s(nums.begin(),nums.end());
        int ans = original;
        while(true){
            if(s.find(ans) == s.end()){
                break;
            }else{
                ans *= 2;
            }
        }

        return ans;
    }
};