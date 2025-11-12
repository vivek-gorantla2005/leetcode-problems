class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();

        // Count 1s
        int ones = 0;
        for (int x : nums) {
            if (x == 1) ones++;
        }

        // If we already have ones
        if (ones > 0) {
            return n - ones;
        }
        
        int ans = INT_MAX;

        for (int i = 0; i < n; i++) {
            int g = nums[i];
            for (int j = i + 1; j < n; j++) {
                g = std::gcd(g, nums[j]);
                if (g == 1) {
                    ans = min(ans, j - i + 1);
                    break;
                }
            }
        }

        if (ans == INT_MAX) return -1;

        return ans - 1 + (n - 1);
    }
};
