class Solution:
    def isPalindrome(self, s: str) -> bool:
        normWord = ""
        for i in range(len(s)):
            if s[i].isalnum():
                normWord += s[i].lower()
        return normWord[-1::-1] == normWord