class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alpha = ""
        for letter in s:
            if letter.isalpha() or letter.isdigit(): 
                s_alpha+= letter
        clean = s_alpha.lower()
        i, j = 0 , len(clean) - 1
        while(i < j ):
            if clean[i]!= clean[j]:
                return False
            i+=1
            j-=1 
        return True