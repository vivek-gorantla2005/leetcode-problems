class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr = nums[:] + nums[:]
        st = []
        ans= [-1] * len(nums)
        for i in range(len(arr)-1,-1,-1):
            while st and st[-1] <= arr[i]:
                st.pop()
            if st:
                ans[i%len(nums)] = st[-1]
            st.append(arr[i])
        return ans
        