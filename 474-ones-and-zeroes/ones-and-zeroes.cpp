class Solution {
public:
    int dfs(vector<string>& strs, int m, int n, int i, vector<vector<vector<int>>>& dp) {
        if (i < 0) return 0;

        if (dp[m][n][i] != -1) return dp[m][n][i];

        // Count zeros and ones in current string
        int mCnt = 0, nCnt = 0;
        for (char c : strs[i]) {
            if (c == '0') mCnt++;
            else nCnt++;
        }

        int notTake = dfs(strs, m, n, i - 1, dp);

        int take = 0;
        if (mCnt <= m && nCnt <= n) {
            take = 1 + dfs(strs, m - mCnt, n - nCnt, i - 1, dp);
        }

        return dp[m][n][i] = max(take, notTake);
    }

    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<vector<int>>> dp(m + 1, vector<vector<int>>(n + 1, vector<int>(strs.size(), -1)));
        return dfs(strs, m, n, strs.size()-1, dp);
    }
};
