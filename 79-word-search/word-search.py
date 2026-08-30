class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols=len(board[0])
        def search(row,col,index,visited):
            if index==len(word):
                return True
            if row<0 or row>=rows or col<0 or col>=cols:
                return False
            if board[row][col]!=word[index]:
                return False
            if (row,col) in visited:
                return False
            visited.add((row,col))
            if search(row+1,col,index+1,visited):
                return True
            if search(row-1,col,index+1,visited):
                return True
            if search(row,col+1,index+1,visited):
                return True
            if search(row,col-1,index+1,visited):
                return True
            visited.remove((row,col))
            return False
        for i in range(rows):
            for j in range(cols):
                visited=set()
                if search(i,j,0,visited):
                    return True
        return False