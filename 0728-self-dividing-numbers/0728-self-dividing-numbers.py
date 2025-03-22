class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result=[]
        for i in range(left,right+1):
            for digit in str(i):
                if int(digit)==0 or i%int(digit)!=0:
                    break
            else:
                result.append(i)
        return result