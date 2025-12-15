class Solution {
public:
    long long getDescentPeriods(vector<int>& prices) {
        long long total = 1;
        long long ans = 1;
        for(int i = 1 ; i < prices.size();i++){
            if(prices[i-1] - prices[i] == 1){
                ans++;
            }
            else{
                ans=1;
            }

            total += ans;
        }

        return total;
    }
};