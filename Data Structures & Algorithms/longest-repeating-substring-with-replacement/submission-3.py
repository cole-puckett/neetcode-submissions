from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''keep track of the character counts within the current window
        and make sure that the window size - the maximum frequency is <= k'''

        charCount = defaultdict(int)
        max_repeated = 0
        left = 0
        result = 0

        for right in range(len(s)):
            charCount[s[right]] += 1
            max_repeated = max(max_repeated, charCount[s[right]])
            
            window = right - left + 1
            while window - max_repeated > k:
                charCount[s[left]] -= 1
                left += 1
                window = right - left + 1
            result = max(result, window)

        return result