class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dicc = {}
        for word in strs:
            wordS = "".join(sorted(word))
            if wordS in dicc:
                dicc[wordS].append(word)
            else:
                dicc[wordS] = [word]
        return list(dicc.values())
        