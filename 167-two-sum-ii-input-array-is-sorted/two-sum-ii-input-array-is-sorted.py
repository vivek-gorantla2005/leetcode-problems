class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        st = 0
        end = len(numbers)-1
        while st <= end:
            s = numbers[st]+numbers[end]
            if s == target:
                return [st+1,end+1]
            elif s > target:
                end-=1
            else:
                st+=1
        return -1
        