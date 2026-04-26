from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loop through the list of strings and map each dictionary to a key in a dictionary of lists

        answer = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord('a')] += 1
            
            answer[tuple(count)].append(word)

        return list(answer.values())