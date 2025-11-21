class Solution {
public:
    int countPalindromicSubsequence(string s) {
        unordered_map<char,int> m;

        for (char c : s) {
            m[c]++;
        }

        set<pair<char,char>> ans;   
        set<char> leftSeen;        

        for (char c : s) {          
            m[c]--;                 

            for (char mid : leftSeen) {
                if (m[mid] > 0) {  
                    ans.insert({mid, c});
                }
            }

            leftSeen.insert(c);
        }

        return ans.size();
    }
};
