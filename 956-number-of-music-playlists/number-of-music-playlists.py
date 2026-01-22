from functools import lru_cache
class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def dp(used_songs: int, length: int) -> int:
            if length == goal:
                return 1 if used_songs == n else 0

            res = 0

            if used_songs < n:
                res += (n - used_songs) * dp(used_songs + 1, length + 1)

            if used_songs > k:
                res += (used_songs - k) * dp(used_songs, length + 1)

            return res % MOD

        return dp(0, 0)
