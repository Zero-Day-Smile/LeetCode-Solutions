class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic={'1':"",
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
        }
        if not digits:
            return []
        result=[""]
        for digit in digits:
            letter=dic[digit]
            temp=[]
            for i in result:
                for j in letter:
                    temp.append(i+j)
                result=temp
        return result