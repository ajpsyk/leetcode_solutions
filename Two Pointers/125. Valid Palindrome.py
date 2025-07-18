class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = ""
        for char in s:
            if char.isalnum():
                cleaned_string += char.lower()
        # iterate over half the string from the start and end
        middle = len(s) // 2
        end = len(s) - 1

        for i in range(0, middle):
            if cleaned_string[i] != cleaned_string[end]:
                return False
            end = end - 1
        return True