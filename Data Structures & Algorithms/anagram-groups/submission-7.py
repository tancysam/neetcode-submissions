class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        wordDict = {}

        for string in strs:
            tmp = [0] * 26
            for ch in string:
                tmp[ord(ch) - ord('a')] += 1
            wordDict.setdefault(tuple(tmp), [])
            wordDict[tuple(tmp)].append(string)

        return list(wordDict.values())
                