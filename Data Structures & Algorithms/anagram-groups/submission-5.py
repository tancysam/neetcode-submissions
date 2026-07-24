class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        wordDict = {}

        for string in strs:
            tmp = [0] * 26
            for ch in string:
                key = ord(ch) - ord('a')
                tmp[key] += 1
            wordDict.setdefault(tuple(tmp), [])
            wordDict[tuple(tmp)].append(string)

        final = []

        for item in wordDict.keys():
            final.append(wordDict[item])

        return final
                