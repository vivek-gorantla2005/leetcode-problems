class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        nextSmallest = [n] * n
        prevSmallest = [-1] * n

        st = []

        # Next Smaller Element
        for i in range(n-1, -1, -1):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()

            if st:
                nextSmallest[i] = st[-1]

            st.append(i)

        st = []

        # Previous Smaller Element
        for i in range(n):
            while st and heights[st[-1]] >= heights[i]:
                st.pop()

            if st:
                prevSmallest[i] = st[-1]

            st.append(i)

        maxi = 0

        for i in range(n):
            width = nextSmallest[i] - prevSmallest[i] - 1
            area = width * heights[i]
            maxi = max(maxi, area)

        return maxi