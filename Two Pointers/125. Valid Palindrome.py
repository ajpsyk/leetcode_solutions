class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = "".join([c for c in s.lower() if c.isalnum()])
        return cleaned_string == cleaned_string[::-1]