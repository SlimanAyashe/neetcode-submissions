class Solution:
    def foundPermutation(self, dictionary1: dict , dictionary2:dict) ->bool:
        for key in dictionary1:
            if dictionary1.get(key) != dictionary2.get(key,-1):
                return False
        return True
    def checkInclusion(self, s1: str, s2: str) -> bool:
        length_s1, length_s2 = len(s1), len(s2)
        if length_s1 > length_s2:
            return False
        s1_dict, s2_dict = {}, {}
        for letter in s1:
            s1_dict[letter] = s1_dict.get(letter, 0) + 1
        
        for i in range(length_s1):
            s2_dict[s2[i]] = s2_dict.get(s2[i],0) + 1

        if self.foundPermutation(s1_dict, s2_dict):
            return True

        for i in range(length_s1, length_s2, 1):
            s2_dict[s2[i-length_s1]] = s2_dict.get(s2[i-length_s1],0) - 1
            s2_dict[s2[i]] = s2_dict.get(s2[i],0) + 1
            if self.foundPermutation(s1_dict, s2_dict):
                return True
        return False
            