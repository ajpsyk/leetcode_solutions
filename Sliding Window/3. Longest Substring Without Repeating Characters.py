class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_chars = set()
        length = 0
        L = 0
        for R in range(len(s)):
            while s[R] in unique_chars:
                unique_chars.remove(s[L])
                L += 1
            unique_chars.add(s[R])
            length = max(length, R - L + 1)
        return max(length, len(unique_chars))