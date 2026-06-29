class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dicc = {}
        j = 0
        for i, word in enumerate(strs):
            wordS = "".join(sorted(word))
            if wordS in dicc:
                result[dicc[wordS]].append(word)
            else:
                result.append([word])
                dicc[wordS] = j
                j += 1
        return result
        