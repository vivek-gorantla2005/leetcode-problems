class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        
        def helper(candidates, idx, target, curr):
            if target == 0:
                self.ans.append(curr[:])   
                return

            if idx == len(candidates):     
                return

            # Take the current number
            if candidates[idx] <= target:
                curr.append(candidates[idx])
                helper(candidates, idx, target - candidates[idx], curr)
                curr.pop()               
            
            helper(candidates, idx + 1, target, curr)

        helper(candidates, 0, target, [])
        return self.ans
