class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        int curr = k;  // allow first 1 to always pass
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == 0){
                curr++;
            } else {
                if(curr < k) return false;
                curr = 0;
            }
        }
        return true;
    }
};
