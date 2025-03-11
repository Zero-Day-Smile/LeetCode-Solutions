class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        l=len(s)
        for i in range(l):
            if s[i]=='(':
                stack.append('(')
            elif s[i]==')':
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    return False
            elif s[i]=='{':
                stack.append('{')
            elif s[i]=='}':
                if stack and stack[-1]=='{':
                    stack.pop()
                else:
                    return False
            elif s[i]=='[':
                stack.append('[')
            elif s[i]==']':
                if stack and stack[-1]=='[':
                    stack.pop()
                else:
                    return False
        return len(stack)==0