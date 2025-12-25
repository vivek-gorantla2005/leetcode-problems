from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        ruleMap = {
            "type": 0,
            "color": 1,
            "name": 2
        }
        
        idx = ruleMap[ruleKey]
        ans = 0
        
        for item in items:
            if item[idx] == ruleValue:
                ans += 1
        
        return ans
