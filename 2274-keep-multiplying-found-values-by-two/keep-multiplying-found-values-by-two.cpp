class Solution {
public:
    int findFinalValue(vector<int>& nums, int original) {
        unordered_set<int>s(nums.begin(),nums.end());
        bool found = false;
        int x = original;
        if(s.find(original) == s.end()){
            return original;
        }else{
            found = true;
        }

        int ans = original;
        while(found){
            ans *= 2;
            if(s.find(ans) == s.end()){
                found= false;
                break;
            }
        }

        return ans;
    }
};