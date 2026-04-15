class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        mini = float('inf')

        for i in range(n):
            # forward direction
            if words[(startIndex + i) % n] == target:
                mini = min(mini, i)

            # backward direction
            if words[(startIndex - i) % n] == target:
                mini = min(mini, i)

        return mini if mini != float('inf') else -1