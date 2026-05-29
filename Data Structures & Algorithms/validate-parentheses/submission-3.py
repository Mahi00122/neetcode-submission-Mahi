class Solution:
    def isValid(self, s: str) -> bool:
        stack  = [] # ) opening h  so (  ye closing hua thats why "opening]":"closing["
        o = { ")" : "(" , 
              "]": "["  ,
              "}": "{"}
        for i in s:
            if i in o:
                if stack and stack[-1] == o[i]:
                    stack.pop()
                
                else:
                    return False
            else:
                stack.append(i)
            #if stack empty return true else false
        return True if not stack else False