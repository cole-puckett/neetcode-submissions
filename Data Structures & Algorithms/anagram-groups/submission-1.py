from collections import Counter, defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # loop through the list of strings and map each dictionary to a key in a dictionary of lists

        answer = defaultdict(list)

        for word in strs:
            anagramKey = tuple(sorted(Counter(word).items()))
            answer[anagramKey].append(word)

        return list(answer.values())