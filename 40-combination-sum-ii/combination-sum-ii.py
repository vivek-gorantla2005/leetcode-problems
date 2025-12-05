class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()
        
        def helper(candidates, idx, target, curr):
            if target == 0:
                self.ans.append(curr[:])   
                return

            if idx == len(candidates):     
                return

            if candidates[idx] <= target:
                curr.append(candidates[idx])
                helper(candidates, idx+1, target - candidates[idx], curr)
                curr.pop()   

            while idx+1 < len(candidates) and candidates[idx+1] == candidates[idx]:
                idx+=1
            
            helper(candidates, idx + 1, target, curr)

        helper(candidates, 0, target, [])
        return self.ans
