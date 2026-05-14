class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen =  dict()
        seen_t = dict()
        if len(s) != len (t):
            return False
        for letter in s:
            if not letter in seen:
                seen[letter] = 0 
            seen[letter] += 1
        for letter in t:
            if not letter in seen_t:
                seen_t[letter] = 0 
            seen_t[letter] += 1
        for key in seen:
            if not key in seen_t or seen[key] != seen_t[key]:
                return False
        return True