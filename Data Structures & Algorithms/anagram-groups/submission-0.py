class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        initialList = {}
        for word in strs:
            sort_word = "".join(sorted(word))
            if initialList and sort_word in initialList:
                initialList[sort_word].append(word)
            else:
                initialList[sort_word] = [word]
        finalList = []
        for wordsList in initialList:
            finalList.append(initialList[wordsList])
        return finalList