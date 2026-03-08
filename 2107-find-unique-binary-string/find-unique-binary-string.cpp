class Solution {
public:
    bool helper(int n, unordered_set<string>& st, string &curr, string &res) {
        if (curr.size() == n) {
            if (st.find(curr) == st.end()) {
                res = curr;
                return true; 
            }
            return false;
        }

        // try '0'
        curr.push_back('0');
        if (helper(n, st, curr, res)) return true;
        curr.pop_back();

        // try '1'
        curr.push_back('1');
        if (helper(n, st, curr, res)) return true;
        curr.pop_back();

        return false;
    }

    string findDifferentBinaryString(vector<string>& nums) {
        unordered_set<string> st(nums.begin(), nums.end());
        string curr, res;
        helper(nums.size(), st, curr, res);
        return res;
    }
};