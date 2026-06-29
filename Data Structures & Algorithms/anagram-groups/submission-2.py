class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublist ={}
        
        for word in strs:
            word_list = [0]*26
            for char in word:
                i = ord(char)-ord("a")
                word_list[i] = word_list[i]+ 1
            word_str = tuple(word_list)
            sublist.setdefault(word_str,[])
            sublist[word_str].append(word)

        
        final = []
        for sublist_key in sublist:
            final.append(sublist[sublist_key])
        
        return final

                
