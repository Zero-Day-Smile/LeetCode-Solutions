class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        news =''.join(char for char in s if char.isalnum())
        return news==news[::-1]
