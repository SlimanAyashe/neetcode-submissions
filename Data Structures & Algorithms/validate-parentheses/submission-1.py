class Solution:
    def sameType(self ,s:str , t:str)-> bool:
        return ( s == '(' and t == ')') or (s == '{' and t == '}') or (s == '[' and t == ']')

    def isValid(self, s: str) -> bool:
        opening_parentheses = ('(','{', '[')
        closing_parentheses = (')', '}', ']')
        stack = []
        for character in s :
            if character in opening_parentheses:
                stack.append(character)
            else:
                if not stack or not self.sameType(stack.pop(), character):
                    return False
        return not stack           