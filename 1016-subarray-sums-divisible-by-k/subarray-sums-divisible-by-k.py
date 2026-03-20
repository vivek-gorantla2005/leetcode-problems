class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix= 0
        res = 0
        prefixCnt = defaultdict(int)
        prefixCnt[0] = 1
        for x in nums:
            prefix+=x
            rem = prefix % k
            if rem in prefixCnt:
                res+=prefixCnt[rem]
            prefixCnt[rem] += 1
        return res

        