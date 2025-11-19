class Solution {
public:
    int solve(vector<int>& nums, int idx,vector<int>&dp) {
        int n = nums.size();
        if (idx >= n - 1) return 0;  

        if(dp[idx] != -1){
            return dp[idx];
        }

        int mini = INT_MAX;

        for (int step = 1; step <= nums[idx]; step++) {
            int next = idx + step;
            if (next < n) {
                int res = solve(nums, next,dp);
                if (res != INT_MAX)
                    mini = min(mini, 1 + res);
            }
        }

        return dp[idx]=mini;
    }

    int jump(vector<int>& nums) {
        vector<int> dp(nums.size(), -1);
        return solve(nums, 0,dp);
    }
};
