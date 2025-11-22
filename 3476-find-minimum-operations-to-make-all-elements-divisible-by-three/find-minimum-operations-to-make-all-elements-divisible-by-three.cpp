class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        int cnt = 0;
        for(int i : nums){
            if(i%3 == 0)continue;
            if((i-1) % 3 == 0 || (i+1)%3 == 0){
                cnt++;
            }
        }
        return cnt;
    }
};