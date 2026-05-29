class Solution:
    def isValid(self, s: str) -> bool:
        for i in s:
            if i ==  "(){}[]"or "[]" or "([{}])":
                return True
            elif i == "[(])":
                return False
        