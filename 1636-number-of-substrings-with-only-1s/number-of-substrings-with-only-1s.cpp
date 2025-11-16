class Solution {
public:
    int numSub(string s) {
        long long ans = 0;
        int cnt = 0;
        int mod = pow(10,9) + 7;
        for(char i : s){
            if(i == '1'){
                cnt++;
            }else{
                cnt = 0;
            }
            ans+=cnt;
        }
        return ans % mod;
    }
};