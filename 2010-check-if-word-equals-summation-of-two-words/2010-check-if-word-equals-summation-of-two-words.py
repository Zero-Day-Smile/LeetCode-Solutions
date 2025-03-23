class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        a=""
        b=""
        c=''
        for i in range(len(firstWord)):
            a+=str(ord(firstWord[i])-97)
        for i in range(len(secondWord)):
            b+=str(ord(secondWord[i])-97)
        for i in range(len(targetWord)):
            c+=str(ord(targetWord[i])-97)
        if int(c)==int(a)+int(b):
            return True
        else:
            return False

