class Solution:
    def isPalindrome(self, s: str) -> bool:
        palindrome = ""
        for i in range(len(s)):
            if s[i].isalnum():
                palindrome += s[i]
        
        palindrome = palindrome.lower()

        for i in range(len(palindrome)):
            if palindrome[i] != palindrome[len(palindrome) - i - 1]:
                return False
        return True